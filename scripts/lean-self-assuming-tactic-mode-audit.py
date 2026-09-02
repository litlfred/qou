"""Candidate self-assuming projections in TACTIC-mode proofs.

`scripts/lean-self-assuming-audit.py` deliberately skips `:= by ...` -- its own
docstring says so ("needs elaboration to judge; out of scope here").  That is a
documented scope limit, NOT a bug in it.  This script probes that area, so the
112-item sizing in bean `qou-z9ws` is read as a lower bound over TERM-mode proofs
rather than as a corpus total.

Candidate-only, same posture as the tool it complements.  Flags a theorem whose
entire tactic block cites nothing but projections off its own instance binder(s).

    THIS SCRIPT HAS ITS OWN BLIND SPOT, AND IT IS THE MOTIVATING CASE.
    ------------------------------------------------------------------
    `QOU.ParticleInteractions.operator_selection_lp` is what prompted this file:

        refine <ctx.x_star_feasible, ?_, ctx.zero_gap>
        intro x hx
        have hgap : ... := ctx.zero_gap
        rw [hgap]
        exact OperatorSelectionLpContext.dual_bound_le_objective x hx

    -- all three conjuncts come from class fields.  This scanner MISSES it.  The
    "no reference outside the binder" rule disqualifies any proof that introduces a
    local (`intro x hx`, `have hgap`), and that is precisely what this one does.

    So 57 is the count of the sub-class with NO local introductions.  The tactic-mode
    population is LARGER and remains unmeasured.  Do not quote 57 as the size of the
    class; quote it as a floor on a sub-class, and say which.

    Recorded rather than fixed because widening the rule to admit locals needs a way
    to tell a local standing in for a field from a local doing real work -- which is
    the elaboration the term-mode tool declined to do, for the same reason.
"""
import re, sys, json
from pathlib import Path

DECL = re.compile(
    r"^(?P<kw>theorem|lemma)\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)"
    r"(?P<sig>.*?):=\s*by\b(?P<body>.*?)(?=^\s*(?:@\[|/--|theorem|lemma|def|structure|class|instance|abbrev|noncomputable|end|namespace|\Z))",
    re.S | re.M)
INST = re.compile(r"\[\s*(?P<n>[A-Za-z_][A-Za-z0-9_']*)\s*:\s*[^\]]+\]")
TACTIC_NOISE = {
 'refine','exact','intro','intros','rw','simp','constructor','apply','have','this',
 'left','right','rfl','trivial','fun','at','with','by','using','and','or','cases',
 'rcases','obtain','subst','omega','ring','linarith','norm_num','positivity','aesop',
 'sorry','decide','show','change','calc','_','set','let','from','id',
}

hits=[]
for f in Path('content').rglob('*.lean'):
    if '.lake' in str(f): continue
    try: src=f.read_text()
    except Exception: continue
    for m in DECL.finditer(src):
        sig, body, name = m.group('sig'), m.group('body'), m.group('name')
        binders=[b.group('n') for b in INST.finditer(sig)]
        if not binders: continue
        # every dotted reference in the body
        refs=re.findall(r"\b([A-Za-z_][A-Za-z0-9_'.]*)", body)
        meaningful=[r for r in refs if r not in TACTIC_NOISE and not r.isdigit()]
        if not meaningful: continue
        proj=[r for r in meaningful if any(r.startswith(b+'.') for b in binders)
              or r.split('.')[0][:1].isupper()]
        # candidate: at least one binder projection, and NOTHING that is a plain
        # lowercase lemma name outside the binder (i.e. no external mathematical input)
        outside=[r for r in meaningful
                 if not any(r.startswith(b+'.') for b in binders)
                 and not r.split('.')[0][:1].isupper()
                 and '.' not in r]
        if proj and not outside:
            hits.append({'file':str(f),'line':src[:m.start()].count('\n')+1,
                         'decl':name,'binders':binders})
print(f"tactic-mode self-assuming CANDIDATES: {len(hits)}")
for h in hits[:25]:
    print(f"  {h['decl']}\n    {h['file']}:{h['line']}  [ctx: {','.join(h['binders'])}]")
Path('/tmp/tacproj.json').write_text(json.dumps(hits, indent=1))
