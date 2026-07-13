import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-surreals-archimedean_seq2.md", "r") as f:
    text = f.read()

replacements = [
    (
        "This conjecture is **not** load-bearing for QOU's main results;\nthe substrate value $q_0$ is generic (not a root\nof unity), so the binary Hoefsmit / char-0 surreal picture applies\nthroughout the main paper. The char-$p$ extension is included\nhere as a conceptual companion: a record of where the same\nHoefsmit machinery would go in the modular setting.",
        "This conjecture is **not** load-bearing for QOU's main results; the substrate value $q_0$ is generic (not a root of unity). The binary Hoefsmit / char-$0$ surreal picture applies throughout this paper. We include the char-$p$ extension here as a conceptual companion. It records how the Hoefsmit machinery maps into the modular setting."
    ),
    (
        "## Note on QOU's main paper",
        "## Note on this paper"
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED: {orig[:100]}")
    text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-surreals-archimedean_seq2.md", "w") as f:
    f.write(text)

