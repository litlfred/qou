with open("../folio-assistant/cat-harness/content/pipeline/qa-criteria-registry.ts", "r") as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if line.strip() == '"conjecture",':
        lines.insert(i+1, '  "milnor",\n  "milnor-section",\n  "milnor-sub-section",')
        break

with open("../folio-assistant/cat-harness/content/pipeline/qa-criteria-registry.ts", "w") as f:
    f.write('\n'.join(lines))
