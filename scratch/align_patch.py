import sys

with open("computations/mass_binding_dashboard.py", "r") as f:
    content = f.read()

align_code = """
def format_md_tables(text):
    lines = text.split('\\n')
    out = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and lines[i].endswith('|') and i+1 < len(lines) and lines[i+1].startswith('|') and '---' in lines[i+1]:
            # Found a table
            table_lines = []
            while i < len(lines) and lines[i].startswith('|') and lines[i].endswith('|'):
                table_lines.append(lines[i])
                i += 1
            # Parse table
            rows = []
            max_cols = 0
            for line in table_lines:
                cells = [cell.strip() for cell in line[1:-1].split('|')]
                max_cols = max(max_cols, len(cells))
                rows.append(cells)
            
            # Compute max widths
            widths = [0] * max_cols
            for r_idx, row in enumerate(rows):
                for c_idx, cell in enumerate(row):
                    if r_idx == 1: continue # skip separator
                    widths[c_idx] = max(widths[c_idx], len(cell))
            
            # Format table
            for r_idx, row in enumerate(rows):
                parts = []
                for c_idx in range(max_cols):
                    cell = row[c_idx] if c_idx < len(row) else ""
                    w = widths[c_idx]
                    if r_idx == 1:
                        # Separator
                        if cell.endswith(':'):
                            if cell.startswith(':'): parts.append(':' + '-'*(max(1, w-2)) + ':')
                            else: parts.append('-'*(max(1, w-1)) + ':')
                        else:
                            parts.append('-'*max(1, w))
                    else:
                        align = '<'
                        if 1 < len(rows) and c_idx < len(rows[1]):
                            sep = rows[1][c_idx]
                            if sep.endswith(':') and not sep.startswith(':'):
                                align = '>'
                        parts.append(f"{cell:{align}{w}}")
                out.append('| ' + ' | '.join(parts) + ' |')
        else:
            out.append(lines[i])
            i += 1
    return '\\n'.join(out)
"""

if "def format_md_tables" not in content:
    content = content.replace("def _ame_table():", align_code + "\ndef _ame_table():")

hook_in = """    _print_legend()"""
hook_out = """    _print_legend()
    import io, sys
    _old_stdout = sys.stdout
    sys.stdout = io.StringIO()"""
if "_old_stdout = sys.stdout" not in content:
    content = content.replace(hook_in, hook_out)

end_in = """    print("\\n  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] "
          "(exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · "
          "B_qCLT_fac=α·(A−1)·⟨bond-type L⟩ · B_magic=2·m_e·A·8G (⁴He). "
          "Defn: standard-part-functor.md.")
    return 0"""
end_out = """    print("\\n  Forms: B_sym=α·ln(tr_free/tr_atom)=α[(Z−1)L_pp+L_pn+(N−1)L_nn] "
          "(exact linear chain, all A) · B_qCLT=α·(A−1)·ℓ̄(D) · "
          "B_qCLT_fac=α·(A−1)·⟨bond-type L⟩ · B_magic=2·m_e·A·8G (⁴He). "
          "Defn: standard-part-functor.md.")
    _out = sys.stdout.getvalue()
    sys.stdout = _old_stdout
    print(format_md_tables(_out), end="")
    return 0"""
if "sys.stdout = _old_stdout" not in content:
    content = content.replace(end_in, end_out)

with open("computations/mass_binding_dashboard.py", "w") as f:
    f.write(content)
