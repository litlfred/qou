import json
d=json.load(open('cert.json'))
F=d['F'];E=d['E'];P=d['paths']
vec=lambda xs: "![" + ", ".join(map(str,xs)) + "]"
out=[]
out.append(f"def fA : Fin 50 → Fin 19 := {vec([f[0] for f in F])}")
out.append(f"def fB : Fin 50 → Fin 19 := {vec([f[1] for f in F])}")
out.append(f"def fC : Fin 50 → Fin 19 := {vec([f[2] for f in F])}")
out.append(f"def eA : Fin 75 → Fin 19 := {vec([e[0] for e in E])}")
out.append(f"def eB : Fin 75 → Fin 19 := {vec([e[1] for e in E])}")
pl=[]
for g in range(50):
    pl.append("[" + ", ".join(f"(({e} : Fin 75), ({s} : ℤ))" for e,s in P[str(g)]) + "]")
out.append("def paths : Fin 50 → List (Fin 75 × ℤ) := ![" + ",\n  ".join(pl) + "]")
open('data.lean','w').write("\n\n".join(out)+"\n")
