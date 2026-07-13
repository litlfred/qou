import fitz
import re
import sys

def sanitize_filename(name):
    # Remove characters that aren't safe for filenames
    name = re.sub(r'[^\w\s-]', '', name)
    # Replace spaces with hyphens
    name = re.sub(r'\s+', '-', name)
    return name.lower()

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 split-pdf-by-chapter.py <input.pdf> <output_dir>")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_dir = sys.argv[2]
    
    doc = fitz.open(input_pdf)
    toc = doc.get_toc()
    
    # We want to extract sections that are level 1 (if not "I ", "II ", etc) or level 2.
    chapters = []
    for item in toc:
        level, title, page = item
        if level == 1:
            if title.startswith("I ") or title.startswith("II ") or title.startswith("III ") or title.startswith("IV "):
                continue
            chapters.append({"title": title, "start": page, "level": level})
        elif level == 2:
            chapters.append({"title": title, "start": page, "level": level})
            
    # Add end pages
    total_pages = doc.page_count
    for i in range(len(chapters)):
        start = chapters[i]["start"] - 1 # 0-indexed
        if i + 1 < len(chapters):
            end = chapters[i+1]["start"] - 1
        else:
            end = total_pages
        chapters[i]["end"] = end
        
    print(f"Found {len(chapters)} chapters to extract.")
    
    for i, chap in enumerate(chapters):
        # some chapters might start on the same page as the next, wait, no, they shouldn't.
        start_idx = chap["start"] - 1
        end_idx = chap["end"] - 1
        
        # if end_idx < start_idx it means the next chapter starts on the SAME page. We still extract that page.
        if end_idx < start_idx:
            end_idx = start_idx
            
        filename = f"{i:02d}-{sanitize_filename(chap['title'])}.pdf"
        out_path = f"{output_dir}/{filename}"
        
        out_doc = fitz.open()
        out_doc.insert_pdf(doc, from_page=start_idx, to_page=end_idx)
        out_doc.save(out_path)
        out_doc.close()
        
        print(f"Saved: {out_path} (Pages {start_idx+1} to {end_idx+1})")
        
if __name__ == "__main__":
    main()
