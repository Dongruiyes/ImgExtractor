import os
import pefile
import shutil
import sys

SUPPORTED_IMAGE_FORMATS = None

def extract_images_from_dll(dll_path, output_dir):
    """
    从 DLL 文件中提取图片资源。

    Args:
        dll_path: DLL 文件的路径。
        output_dir: 提取的图片资源的输出目录。
    """
    try:
        pe = pefile.PE(dll_path)

        # 检查 DLL 文件是否包含资源
        if not hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
            return

        # 遍历资源目录
        for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
            if hasattr(resource_type, 'directory'):
                for resource_id in resource_type.directory.entries:
                    if hasattr(resource_id, 'directory'):
                        for resource_lang in resource_id.directory.entries:
                            if hasattr(resource_lang, 'data'):
                                data = pe.get_data(resource_lang.data.struct.OffsetToData, resource_lang.data.struct.Size)
                                # 检查数据是否为支持的图片格式
                                for ext in SUPPORTED_IMAGE_FORMATS:
                                    if data.startswith(get_magic_bytes(ext)):
                                        output_path = os.path.join(output_dir, f"{os.path.basename(dll_path)}_{resource_lang.data.struct.OffsetToData}{ext}")
                                        with open(output_path, 'wb') as f:
                                            f.write(data)
                                        print(f"Extracted image: {output_path}")
                                        m_statusBar2.SetStatusText(f"Extracted: {os.path.basename(output_path)}")
                                        break

    except pefile.PEFormatError:
        m_statusBar2.SetStatusText(f"Error: Not a valid PE file.")
    except Exception as e:
        m_statusBar2.SetStatusText(f"Error processing: {os.path.basename(dll_path)}")

def get_magic_bytes(ext):
    """
    获取不同图片格式的魔术字节。
    """
    if ext in ('.jpg', '.jpeg'):
        return b'\xFF\xD8\xFF'
    elif ext == '.png':
        return b'\x89PNG\r\n\x1a\n'
    elif ext == '.gif':
        return b'GIF87a'  # 或 GIF89a
    elif ext == '.webp':
        return b'RIFF'
    elif ext == '.bmp':
        return b'BM'
    elif ext in ('.tiff', '.tif'):
        return b'II*\x00'  # 或 MM\x00*
    elif ext == '.svg':
        return b'<svg'
    elif ext in ('.heif', '.heic'):
        return b'ftypheic'  # 或 ftypheix, ftypmif1, ftypmsf1
    elif ext == '.psd':
        return b'8BPS'
    elif ext == '.raw':
        # RAW 格式有多种不同的魔术字节，这里仅列出一种常见的
        return b'II\x1a\x00\x00\x00HEAPCCDR'
    elif ext == '.ico':
        return b'\x00\x00\x01\x00'
    return b''

def main(target_path, output_directory):

    os.makedirs(output_directory, exist_ok=True)  # 确保输出目录存在

    if os.path.isfile(target_path):
        # 如果是文件，直接处理
        if target_path.lower().endswith('.dll'):
            m_statusBar2.SetStatusText(f"Processing: {os.path.basename(target_path)}")
            extract_images_from_dll(target_path, output_directory)
        elif target_path.lower().endswith(tuple(SUPPORTED_IMAGE_FORMATS)):
            m_statusBar2.SetStatusText(f"Copying: {os.path.basename(target_path)}")
            output_path = os.path.join(output_directory, os.path.basename(target_path))
            if os.path.abspath(target_path) != os.path.abspath(output_path):
                shutil.copy2(target_path, output_path)
            else:
                m_statusBar2.SetStatusText(f"Skipping: {os.path.basename(target_path)}")

    elif os.path.isdir(target_path):
        # 如果是目录，遍历目录
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.lower().endswith('.dll'):
                    dll_path = os.path.join(root, file)
                    m_statusBar2.SetStatusText(f"Processing: {os.path.basename(dll_path)}")
                    extract_images_from_dll(dll_path, output_directory)
                elif file.lower().endswith(tuple(SUPPORTED_IMAGE_FORMATS)):
                    image_path = os.path.join(root, file)
                    m_statusBar2.SetStatusText(f"Copying: {os.path.basename(image_path)}")
                    output_path = os.path.join(output_directory, file)
                    if os.path.abspath(image_path) != os.path.abspath(output_path):
                        shutil.copy2(image_path, output_path)
                    else:
                        m_statusBar2.SetStatusText(f"Skipping: {os.path.basename(image_path)}")

if __name__ == "__main__":

    if len(sys.argv) > 2:
        target_path = sys.argv[1]
        output_directory = sys.argv[2]
        main(target_path, output_directory)
    else:
        print("Usage: python ImgExtractor.py <target_path> <output_directory>")