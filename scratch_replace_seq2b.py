import re

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-mass-binding-algorithms_seq2.md", "r") as f:
    text = f.read()

pattern = r"\*The categorical action is \*\*fibre-independent\*\*: it depends only\s+on the rigid-monoidal structure of \$\\mathbf\{C\}\$, not on the choice\s+of fibre functor \$\\tau\$\. The archimedean specialisation enters at\s+Step 9 \(mass identity\) via the Markov trace evaluation at \$q_0\$\.\*"

repl = r"*The categorical action is **fibre-independent**. It depends strictly on the rigid-monoidal structure of $\mathbf{C}$, independent of the fibre functor $\tau$. Archimedean specialisation enters at Step 9 (mass identity) via Markov trace evaluation at $q_0$.*"

new_text, num = re.subn(pattern, lambda m: repl, text, flags=re.MULTILINE)
if num == 0:
    print("FAILED")
else:
    print(f"REPLACED {num} occurrences.")

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-mass-binding-algorithms_seq2.md", "w") as f:
    f.write(new_text)
