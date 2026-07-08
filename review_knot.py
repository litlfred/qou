import json
import datetime
import subprocess

file_path = "content/quantum-observable-universe/appendix-knot-operations/knot-operator-basis-table-intro.qa.json"
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
    "fit-section-chapter": "Fits perfectly as table documentation in the knot operations appendix.",
    "da-false-claim": "No claims made, just documentation.",
    "da-vacuous": "Sufficient to explain the tables.",
    "da-circular": "No circular reasoning.",
    "da-overclaim": "No claims made.",
    "da-hidden-dof": "Parameters (b_i, b_j, h) clearly specified.",
    "da-non-sequitur": "Flows logically.",
    "da-lean-narrative-divergence": "N/A - table documentation.",
    "da-citation-misuse": "N/A",
    "da-definitional-ambiguity": "Terms like normal-form (NF) and Hecke amplitude are clearly defined.",
    "da-empirical-fragility": "N/A",
    "da-physical-implausibility": "N/A",
    "da-reproducibility": "N/A - explanatory text.",
    "da-referee-verdict": "Clear documentation for the tables."
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

print("Reviewed knot-operator-basis-table-intro block.")
