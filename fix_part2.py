import json
def append_to_file(fname, content):
    p = f"/Users/litlfred/space_cats/qou/amalgamated_done/{fname}"
    with open(p, "a") as f: f.write(content)

from fluid_part2 import content2
append_to_file("fluid-dynamics_seq6.md", content2)
