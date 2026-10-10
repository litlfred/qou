# Retired overnight drivers

Moved here from `computations/` on 2026-10-05, by owner decision on bean
`qou-hmji` (story TOOLS T6b). They are moved, not deleted.

None of the three could run as written:

- `run-k8-overnight.sh` and `run-overnight-mac.sh` call
  `python3 hecke_characters.py` from `computations/`. That script now lives at
  `computations/hecke/hecke_characters.py`, so both exit at their first step.
- `run-sage-witnesses.sh` documents itself as `./scripts/run-sage-witnesses.sh`
  after `./scripts/setup-sage.sh`. Neither path exists. None of the three
  witnesses it promises (`computations/sage-*.witness.json`) is in the tree.
  Its inputs, `computations/sage-{borromean-gA,cgeom,nuclear-braid}.sage`, stay
  where they are.

Their committed outputs, `computations/hecke-k*.json`, are untouched. No content
block names any of them as a witness, so the producer Tools in `tool-defs/` do
not reach them.

Long-running regeneration now goes through
`processes/content/witness-refresh.bpmn`, with the owner's approval step.
