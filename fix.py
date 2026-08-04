import re

with open('content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceH4.lean', 'r') as f:
    orig = f.read()

with open('/tmp/MarkovTraceH4Gram.lean', 'r') as f:
    gram = f.read()

# Extract from theorem gramval_0_0 down to end of gram_symm_proved
start_idx = gram.find("theorem gramval_0_0")
end_idx = gram.find("/-- **(M2)")

gram_lemmas = gram[start_idx:end_idx].strip()
gram_lemmas = gram_lemmas.replace("gram_symm_proved", "gram_symm")

# Replace sorry in orig
sorry_regex = re.compile(r'theorem gram_symm \(z h : R\) :\n    ∀ i j, trM z h \(mulNF h \(e i\) \(e j\)\) = trM z h \(mulNF h \(e j\) \(e i\)\) := by\n  sorry')

new_content = orig[:sorry_regex.search(orig).start()] + gram_lemmas + "\n\n" + orig[sorry_regex.search(orig).end():]

with open('content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceH4.lean', 'w') as f:
    f.write(new_content)
