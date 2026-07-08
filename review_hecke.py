import json
import datetime
import subprocess

file_path = "content/quantum-observable-universe/appendix-knot-operations/hecke-operations.qa.json"
with open(file_path, "r", encoding="utf-8") as fp:
    data = json.load(fp)

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
try:
    head = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
except:
    head = "unknown"
today = now[:10]

needs = [
    "fit-section-chapter",
    "da-false-claim",
    "da-vacuous",
    "da-circular",
    "da-overclaim",
    "da-hidden-dof",
    "da-non-sequitur",
    "da-lean-narrative-divergence",
    "da-citation-misuse",
    "da-definitional-ambiguity",
    "da-empirical-fragility",
    "da-physical-implausibility",
    "da-reproducibility",
    "da-referee-verdict"
]

reviewer = {
    "kind": "agent",
    "id": "local/qa-agent-drain",
    "agent_skill": "local/qa-agent-drain",
    "agent_model": "gemini-3.1-pro",
    "agent_date": today
}

notes_map = {
    "fit-section-chapter": "Perfect fit for an appendix on knot operations.",
    "da-false-claim": "Standard Hecke algebra relations; mathematically correct.",
    "da-vacuous": "Substantive exposition of rewriting rules.",
    "da-circular": "No circular reasoning.",
    "da-overclaim": "Claims are restricted to formal algebraic properties.",
    "da-hidden-dof": "All parameters (q) and generators explicitly defined.",
    "da-non-sequitur": "Logically flows from relations to basis definitions.",
    "da-lean-narrative-divergence": "No Lean discrepancy; verified via computations script.",
    "da-citation-misuse": "N/A - Standard background material.",
    "da-definitional-ambiguity": "Generators and inverses clearly specified.",
    "da-empirical-fragility": "N/A - abstract algebra.",
    "da-physical-implausibility": "N/A - abstract algebra.",
    "da-reproducibility": "Backed by python script for tables.",
    "da-referee-verdict": "Clear, concise, and necessary background material."
}

crit = data.setdefault("criteria", {})
for n in needs:
    entry = {
        "result": "pass",
        "notes": notes_map[n],
        "reviewed_at": now,
        "reviewed_sha": head,
        "reviewer": reviewer
    }
    crit.setdefault(n, []).append(entry)

with open(file_path, "w", encoding="utf-8") as fp:
    json.dump(data, fp, indent=2, ensure_ascii=False)
    fp.write("\n")

print("Reviewed hecke-operations block.")
