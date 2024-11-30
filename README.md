# UTF-8 Cleaner

一个简单的工具,用于将非UTF-8编码的文本转换为UTF-8格式,同时保持内容不变。特别适用于需要将pytest测试输出结果粘贴到Claude等要求UTF-8格式的场景。

## 安装

1. 确保已安装Python 3.6+
2. 安装依赖:
```bash
pip install -r requirements.txt
```

## 使用方法

1. 使用命令行参数指定输入输出文件:
```bash
python utf8_cleaner.py -i input.txt -o cleaned_output.txt
```

2. 直接通过管道传入文本:
```bash
pytest | python utf8_cleaner.py -o cleaned_output.txt
```

3. 从标准输入读取并输出到标准输出:
```bash
python utf8_cleaner.py
```
(输入文本后按Ctrl+Z然后回车来结束输入)

## 命令行参数

- `-i` 或 `--input`: 指定输入文件路径（可选）
- `-o` 或 `--output`: 指定输出文件路径（可选）

如果不指定输入文件，程序将从标准输入读取
如果不指定输出文件，程序将输出到标准输出

## 功能特点

- 自动检测输入文本的编码
- 支持多种常见编码(UTF-8, GBK, GB2312, ASCII, ISO-8859-1等)
- 优雅处理无法识别的字符
- 保持原始文本格式和内容不变
- 输出UTF-8格式的文本
