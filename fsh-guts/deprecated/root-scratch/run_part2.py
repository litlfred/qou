import json
def append_to_file(fname, content):
    p = f"/Users/litlfred/space_cats/qou/amalgamated_done/{fname}"
    with open(p, "a") as f: f.write(content)

with open("fluid_part2.py") as f:
    text = f.read()

# Execute it without the last line
exec(text.replace('append_to_file("fluid-dynamics_seq6.md", content2)', ''))

append_to_file("fluid-dynamics_seq6.md", content2)
