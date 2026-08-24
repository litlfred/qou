---
# qou-maz5
title: 'z2bn Q0_FLIP: the ideal_muon entry was generated from a tree without the fix that made it proton'
status: todo
type: task
created_at: 2026-08-24T07:15:36Z
updated_at: 2026-08-24T07:15:36Z
---

NOT ACTIONED BY ME ON PURPOSE. The manifest is a CONTROL INPUT
(q0_producer_pin_classifier.py's own doctrine): removing z2bn from `ideal_muon`
re-pins a producer, which that script calls "a decision, not a sweep". This is
bean qou-bdkx's live territory -- 4 commits within the last day -- so the
finding is recorded here rather than flipped by a passing branch.

WHAT THE AUDIT SEES
  q0_anchor_consistency_audit: Q0_FLIP = 1
    z2bn-tau-derivation-probe.witness.json
      anchor=proton (declared) but q0Value=1.10997859555733... (MUON)
      expected 1.109978582751... (proton)

THE MECHANISM, IN ORDER (all timestamps UTC)
  08-23 08:50  witness: q0Anchor=independent, no q0Value. q0 was a HARDCODED
               literal -- the muon 50-digit value -- under a comment saying
               proton.
  08-23 09:00  2ee9a5169 (bean qou-bdkx) fixes exactly that: reads
               `q_parameter.Q_MP` instead of typing a literal, declares
               q0Anchor=proton, records q0Value. VERIFIED at that commit the
               witness carried the PROTON value 1.1099785827513808075916.
               The fix was correct and internally consistent.
  08-23 16:58  ea82e980e / 8b4825920 regenerate q0_anchor_manifest.json
               ("the producer lookup was root-only, so half the corpus was
               invisible"). z2bn goes from ABSENT to `ideal_muon`.
               `git merge-base --is-ancestor 2ee9a5169 ea82e980e` -> NO.
               The regeneration ran on a tree that did NOT contain the fix, so
               it classified z2bn from the PRE-FIX witness -- the one written
               while q0 was the hardcoded muon literal.
  08-24        my drain re-runs the producer. q_parameter now stem-resolves
               z2bn to muon (because the manifest says so), so Q_MP returns
               the MUON value while the producer still declares proton.
               THE DRAIN DID NOT CAUSE THIS -- it made a latent contradiction
               observable by regenerating a witness that had gone stale
               before the manifest changed under it.

WHY I BELIEVE THE ENTRY IS A FOSSIL, NOT A DECISION
  q0_producer_pin_classifier.py's docstring: "(This corrects the first version
  of this script, which treated the manifest as a passive registry and would
  have proposed 26 `ideal_muon` additions -- silently re-pinning 26
  producers.)" z2bn's entry arrived in exactly that window, by exactly that
  kind of regeneration.
  Against it stand: the producer's own declaration (proton), its
  q0AnchorReason naming "q_parameter.Q_MP, the canonical proton pin", the
  sibling lever1 producer's comment citing "the 2026-08-07 owner directive
  that all production code defaults to the experimental/proton anchor", and
  lever1's own manifest bucket (physical_proton).

IF THE FOSSIL READING IS RIGHT, THE FIX IS
  move z2bn_tau_derivation_probe from ideal_muon -> physical_proton, re-run
  computations/substrate/z2bn_tau_derivation_probe.py, Q0_FLIP 1 -> 0.
  Do NOT hand-edit the witness: the value follows the manifest, not the label.

CONTEXT: NOT AN ISOLATED CASE
  q0_producer_pin_classifier.py --show 200 reports 11 producers where "code
  says one pin, witness records the other", several with "hardcoded muon
  50-digit" -- the same defect class z2bn's fix was written to close.
