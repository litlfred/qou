# Type-B Folded Crystal Infrastructure Roadmap

**Goal:** Implement Composite 3 (`Type-B folded crystal sum`) to definitively resolve the $c_3$ keystone and unlock 1ppQ accuracy.
**Estimated Scope:** 12-17 sessions.

## Python Implementation (Combinatorics & Evaluation)
- [ ] Implement $B_n$ Cartan Datum and weight space logic.
- [ ] Implement Kashiwara-Nakashima (KN) tableaux for Type-B crystals.
- [ ] Implement Kashiwara operators ($e_i, f_i$) on KN tableaux.
- [ ] Implement connected component generation for highest weight crystals $B(\lambda)$.
- [ ] Implement the content statistic $c(T)$ and evaluate the composite sum $F(u) = \sum_{T} q_0^{c(T)} u^{|T|}$.
- [ ] Validate against CAL-3 anchor ($c_3 \approx -2.07$).

## Lean 4 Implementation (Formalism & Rigor)
- [ ] Define abstract `CartanDatum` and `CrystalGraph` typeclasses (stubbed).
- [ ] Formalize $B_n$ root system and Cartan matrix.
- [ ] Formalize Type-B Kashiwara-Nakashima tableaux.
- [ ] Prove Kashiwara operator tensor product rules.
- [ ] Connect folded crystal structure to matter/antimatter chirality (§7b).
