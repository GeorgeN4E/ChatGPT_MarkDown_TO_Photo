#North America 8x 10 print layout
#website 

#<div style="page-break-before: always;"></div> 
#page break


import re
import sys

def convert_equations(content):
    r"""
    Convert LaTeX equations from \[...\] format to $$...$$ format
    Convert LaTeX equations from \(...\) format to $$...$$ format
    """
    pattern = re.compile(r'\\\[(.*?)\\\]', re.DOTALL)
    part1=pattern.sub(r'$$\1$$', content)

    pattern = re.compile(r'\\\((.*?)\\\)', re.DOTALL)


    return pattern.sub(r'$$\1$$', part1)

def main():
    input_file = "curs1-6.md"
    output_file = "outcurs1-6.md"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    converted_content = convert_equations(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(converted_content)

if __name__ == "__main__":
    main()