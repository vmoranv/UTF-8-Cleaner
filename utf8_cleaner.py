import sys
import chardet
import argparse

def detect_and_convert_to_utf8(input_text):
    """
    检测输入文本的编码并转换为UTF-8格式
    """
    # 如果输入已经是字符串,先编码为bytes
    if isinstance(input_text, str):
        input_bytes = input_text.encode('utf-8', errors='ignore')
    else:
        input_bytes = input_text

    # 检测编码
    result = chardet.detect(input_bytes)
    detected_encoding = result['encoding']
    
    # 如果检测失败,使用常见编码尝试解码
    if not detected_encoding:
        common_encodings = ['utf-8', 'gbk', 'gb2312', 'ascii', 'iso-8859-1']
        for encoding in common_encodings:
            try:
                return input_bytes.decode(encoding)
            except UnicodeDecodeError:
                continue
        return input_bytes.decode('utf-8', errors='ignore')
    
    # 使用检测到的编码解码
    try:
        return input_bytes.decode(detected_encoding)
    except UnicodeDecodeError:
        # 如果解码失败,使用UTF-8 with ignore选项
        return input_bytes.decode('utf-8', errors='ignore')

def main():
    parser = argparse.ArgumentParser(description='将文本转换为UTF-8格式')
    parser.add_argument('-i', '--input', help='输入文件路径', required=False)
    parser.add_argument('-o', '--output', help='输出文件路径', required=False)
    args = parser.parse_args()

    # 从文件或标准输入读取
    if args.input:
        with open(args.input, 'rb') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.buffer.read()
    
    # 转换为UTF-8
    cleaned_text = detect_and_convert_to_utf8(input_text)
    
    # 输出到文件或标准输出
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
    else:
        sys.stdout.write(cleaned_text)

if __name__ == "__main__":
    main()
