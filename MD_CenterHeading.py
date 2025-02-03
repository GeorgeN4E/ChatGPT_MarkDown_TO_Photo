import re

def center_headings(md_text):
    def replacer(match):
        level = len(match.group(1))  # Determine heading level
        text = match.group(2)
        
        # Make bold if text contains **bold**
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        
        return f'<div align="center"><h{level}>{text}</h{level}></div>\n'
    
    # Match ### and #### headings while keeping them in HTML format
    centered_md = re.sub(r'(?m)^(#{3,4}) (.*)', replacer, md_text)
    return centered_md

# Example usage
if __name__ == "__main__":
    input_file = "Curs1-12 fara center.md"
    output_file = "v3 Curs1-12 centered.md"
    
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_text = f.read()
    
    centered_text = center_headings(markdown_text)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(centered_text)
    
    print(f"Processed Markdown saved to {output_file}")
