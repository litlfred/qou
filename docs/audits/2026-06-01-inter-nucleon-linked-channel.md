# Inter-nucleon LINKED channel: braid word, Markov trace, writhe — testing the census lead

**Date:** 2026-06-01
**Branch:** `claude/inter-nucleon-linked-channel-2026-06-01`
**Scope:** Test the single most-promising DERIVED lead of the knot-operator
census ([`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md),
PR #1677): the **inter-nucleon LINKED channel** (writhe pp=+1/nn=−1,
non-Brunnian) that escapes BOTH Borromean obstructions. DERIVE its braid
word, Markov trace, and writhe; test (1) the 5↔3 Markov-destabilization
bridge and (2) the U(1)_framing.
**Compute:**
[`inter_nucleon_linked_channel.py`](../../computations/inter_nucleon_linked_channel.py),
witness
[`inter-nucleon-linked-channel.witness.json`](../../computations/inter-nucleon-linked-channel.witness.json)
(audit-only, RAW @ 60 dps + symbolic-in-q, 10 assertions pass). **No tuning
to m_n−m_p, B_AME, hypercharge, spin, or any h^k.**

---

## VERDICT (one line)

**Verdict (c)-with-precise-obstruction, leaning (b)+(partial-a): the linked
channel = the Hopf link `T(2,±2) = σ₁^{±2}` DOES escape both Borromean
obstructions — it is non-Brunnian (linking number ±1 ≠ 0) and carries a
nonzero writhe (±2), so its U(1)_framing is LIVE (unlike the writhe-0
Borromean) — and its braid word DOES contain a cleanly Markov-destabilizable
single crossing (`tr_M(σ₁) = z` exactly, trace-invariant), which the Brunnian
Borromean lacks. BUT neither obstruction-escape closes the keystone: (i) the
destabilization is the 2↔1 strand move WITHIN the m=2 torus tower, NOT a
derived 5→3 functor onto the 3-strand Borromean H₃ trace — the linked channel
lives on 2 strands, not 5, so it does not bridge the fiber level to the
baryon trace; and (ii) the framing factor `q^{w·c}` EXISTS and is nontrivial
(pp/nn differ), but `writhe → hypercharge Y` is still UNDEFINED — with the
natural per-crossing coupling `c=1` the pp/nn framing difference (0.420)
misses the PDG m_n−m_p/m_p split (0.00138) by ~305×, confirming there is no
accidental fit and that Y is not derivable from the framing without an
unjustified coupling choice. CLEAN result: the channel supplies a derived
LIVE U(1) and a derived destabilizable crossing, but NOT the 5↔3 bridge and
NOT a hypercharge.**

---

## 1. The braid word (DERIVED, with provenance)

| Channel | Braid word `𝓑` | Torus | `B_n` | Generators | Writhe `w` | Linking `lk` |
|---|---|---|---|---|---|---|
| **pp** | `σ₁²` | `T(2,2)` (positive Hopf) | `B₂ = ℤ` | `{σ₁}` | **+2** | **+1** |
| **nn** | `σ₁⁻²` | `T(2,−2)` (mirror Hopf) | `B₂ = ℤ` | `{σ₁}` | **−2** | **−1** |
| **pn** | `𝟙` | `T(2,0)` (2-cpt unlink) | `B₂` | `{}` | **0** | **0** |

**Strand count: 2.** **Braid group: `B₂ = ℤ` (single generator `σ₁`).**
**Hecke algebra: `H₂(q)`, Wedderburn blocks `(2)` and `(1,1)`.**

### Provenance (NOT a fit)

The braid word is DERIVED, not chosen:

1. The inter-nucleon arc (gen `3k+2`,
   [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md))
   **links two nucleon color-tube components**. A linked (non-Brunnian)
   inter-nucleon operator is the lead's premise.
2. Per
   [`fermion-boson-knot-link.md`](../../content/quantum-observable-universe/particle-interactions/fermion-boson-knot-link.md),
   the framework's **2-component LINK sector IS the `T(2,n)`-even (Hopf)
   family**: "two components, one winds +1 and the other −1 around the Reeb
   direction." The MINIMAL non-Brunnian 2-component link is the **Hopf link
   `T(2,2) = σ₁²`** (linking number 1).
3. Chirality (matter–matter vs matter–antimatter, the `ε` sign rule of the
   color-tube conjecture) fixes the sign: `pp → σ₁^{+2}`, `nn → σ₁^{−2}`
   (mirror), `pn → 𝟙` (unlinked / averaged).

**The census's "writhe pp=+1/nn=−1" is the LINKING NUMBER `lk(Hopf^{±}) =
±1`** (the production single-crossing assignment's linking-number shadow);
the full Hopf diagram's **writhe is ±2**. Both are reported raw. No numeric
is tuned to any target.

## 2. The Markov trace `tr_M(ρ(𝓑)) = J_𝓑(q)`

Canonical **Wenzl / Jones-Markov** trace on `H₂(q)` (mass-formula
convention): the unique trace with `tr_M(𝟙)=1` and
`tr_M(β·σₙ) = z·tr_M(β)`, `z = 1/(q^{1/2}+q^{-1/2})`. Decomposing on the two
1-dim blocks `(2)` (`σ₁ ↦ q`) and `(1,1)` (`σ₁ ↦ −q⁻¹`):

```
tr_M(σ₁^k) = W_(2)·q^k + W_(1,1)·(−q⁻¹)^k
```

with Wenzl weights fixed by the two Markov axioms:

```
W_(2)   = (q^{3/2} + q + 1)/(q³ + q² + q + 1)         W_(2)(q₀)   = 0.69633…
W_(1,1) = (q³ + q² − q^{3/2})/(q³ + q² + q + 1)       W_(1,1)(q₀) = 0.30367…
```

**Trace values (RAW @ 60 dps, q₀ = 1.10997859…):**

| Channel | `tr_M` symbolic | `tr_M(q₀)` | `(2)` block | `(1,1)` block |
|---|---|---|---|---|
| **pp** `σ₁²` | `W_(2)q² + W_(1,1)q⁻²` | **1.104388069861502…** | 0.857909… | 0.246479… |
| **nn** `σ₁⁻²` | `W_(2)q⁻² + W_(1,1)q²` | **0.939318148412961…** | 0.565175… | 0.374143… |
| **pn** `𝟙` | `W_(2) + W_(1,1) = 1` | **1** (exact) | 0.696325… | 0.303675… |

- **Both Wedderburn blocks `(2)` and `(1,1)` carry weight** (no block
  vanishes); block sums equal the full trace to 1e-50 (asserted).
- **The trace is NOT bar-symmetric:** `tr_M(pp) ≠ tr_M(nn)`
  (`tr_M(pp) − tr_M(nn) = +0.16507…`). The Wenzl Jones-Markov trace carries
  the framing/writhe, so the matter-matter (pp) vs matter-antimatter (nn)
  linking gives a genuine RAW trace asymmetry — reported, not tuned.
- **Cross-validation against the merged census:** `tr_M(σ₁²)` equals the
  census's Hopf closed form `1 + (q−1)/√q` **to 0.0 at 60 dps** — an exact
  agreement that validates both this Wenzl computation and the census's Hopf
  entry.

## 3. Writhe + non-Brunnian (CLAIM verification)

- **Writhe** (RAW, sum of crossing signs): pp `+2`, nn `−2`, pn `0`
  (asserted). **Linking number**: pp `+1`, nn `−1`, pn `0` (asserted). The
  census's pp=+1/nn=−1 is the linking number; the full writhe is ±2.
- **Non-Brunnian: confirmed.** The Hopf link has linking number ±1 ≠ 0 — its
  two components are genuinely linked. Brunnianness (every proper sublink
  trivial) requires ≥3 components with `lk=0` on each 2-sublink, as the
  Borromean has. The Hopf link fails both: **it ESCAPES the Borromean
  Brunnian obstruction.**

## 4. CLAIM 1 — Markov destabilization (the 5↔3 bridge)

**Partially derived; bridge NOT closed.**

- **Single crossing destabilizes cleanly (trace-invariant):**
  `tr_M(σ₁) = z(q₀) = 0.4993203340329180…` — matches the Markov-axiom-3
  factor `z` to 1e-45 (asserted). So a single `σ₁^{±1}` IS a clean
  destabilization `H₂ → H₁` with the canonical `z^{±1}` scaling: the Markov
  move is trace-invariant exactly as required.
- **The linked channel ESCAPES the Brunnian destabilization block.** The
  Borromean `(σ₁⁻¹σ₂)³` in `B₃` uses BOTH generators and is Brunnian: no
  trailing single `σ₂^{±1}` is disjoint, so it admits **no** clean
  destabilization (census §3a). The linked channel's word `σ₁^k` **does**
  contain destabilizable single crossings — so it is not blocked the way the
  Borromean is.
- **BUT the destabilization is the wrong direction for the keystone.** The
  Hopf word `σ₁²` does NOT destabilize in one move (it is two crossings on
  the **same** strand pair — a Reidemeister-II / conjugation reduction within
  `H₂`, not a `β·σₙ^{±1}` with `β` disjoint; the one-move prediction
  `z·tr_M(σ₁)` misses `tr_M(σ₁²)` by 0.855, RAW). And critically the linked
  channel lives on **2 strands**, so its destabilization is the **2↔1 move
  within the `m=2` torus tower** — it is NOT the missing **5→3** functor onto
  the 3-strand Borromean `H₃` trace. The 5-strand `S₅`/SO(3) fiber level and
  the 3-strand baryon trace are untouched by a 2-strand object.

**Conclusion for Claim 1:** the linked channel supplies a DERIVED, clean,
trace-invariant Markov destabilization (escaping the Brunnian block) — but
in the `m=2` torus tower, NOT as the 5↔3 fiber→baryon bridge the s5-so3 /
flavor-cusp audits name. **The 5↔3 bridge stays OPEN.**

## 5. CLAIM 2 — U(1)_framing on nonzero writhe

**Live U(1) derived; hypercharge NOT derived.**

The Reidemeister-I framing anomaly multiplies the trace by `q^{w·c}` (`w` =
writhe, `c` = per-crossing framing coupling). At the observable level
`Im(q₀)=0` (CLAUDE.md), so `q^{w·c}` is a real framing FACTOR, not a complex
phase. With `c=1` (SET, not fitted):

| Channel | writhe `w` | framing `q^{w·c}` (q₀, c=1) |
|---|---|---|
| pp | +2 | **1.232052…** |
| nn | −2 | **0.811654…** |
| pn | 0 | 1 (trivial) |

- **The framing U(1) is LIVE** on the linked channel (writhe ±2 ≠ 0), unlike
  the writhe-0 Borromean baryon. The pp/nn framing factors DIFFER
  (`f_pp − f_nn = 0.420399…`) — a derived candidate for an isospin/hypercharge
  split DATUM.
- **But `writhe → Y` is UNDEFINED.** `w` is an integer braid invariant; `Y`
  is a continuous charge; no canonical map is supplied. **Falsification
  check:** the pp/nn framing difference 0.420399 vs the PDG
  `(m_n−m_p)/m_p = 0.00137842` differs by **~305×**. The framing factor with
  `c=1` does NOT reproduce the mass split — confirming there is **no
  accidental fit**, and that choosing `c` to make them agree would be exactly
  the fit the discipline review catches. A framing factor EXISTING is not a
  hypercharge assignment.

**Conclusion for Claim 2:** the linked channel carries a DERIVED, nontrivial
U(1)_framing (the pp/nn trace + framing asymmetry is real and raw) — but the
identification of that U(1) with hypercharge Y remains UNDEFINED.

## 6. Verdict per (a)/(b)/(c)/(d)

| | Question | Answer |
|---|---|---|
| **(a)** | Supplies the derived 5↔3 Markov-destabilization bridge? | **NO** (partial): supplies a clean trace-invariant destabilization that escapes the Brunnian block, but it is the **2↔1** torus-tower move, not the **5→3** fiber→baryon functor. The 5↔3 bridge stays OPEN. |
| **(b)** | Carries a derived U(1)? | **YES**: writhe ±2 ≠ 0 → live U(1)_framing `q^{w·c}`, nontrivial and pp/nn-asymmetric — escaping the writhe-0 Borromean obstruction. But `writhe → Y` is UNDEFINED (misses PDG by ~305× at c=1). |
| **(c)** | Both? | **Partially**: escapes BOTH obstructions (non-Brunnian + nonzero writhe), as the census predicted — but escaping the obstructions does NOT close either keystone (no 5→3 functor; no hypercharge). |
| **(d)** | Neither, with precise obstruction? | The precise residual obstructions: **(i)** strand-count mismatch — the linked channel is 2-strand, the bridge needs 5→3; **(ii)** writhe (integer) → Y (continuous) map is undefined and not fittable without an unjustified coupling. |

**Net:** the census's lead is **confirmed in its premise** (a linked,
non-Brunnian, nonzero-writhe operator exists and escapes both Borromean
obstructions) and **honest in its limits** (escaping the obstructions is
necessary but not sufficient — the 5↔3 bridge and the hypercharge are still
open). This is a clean "(b) ✓ live U(1) derived + (partial a) destabilizable
crossing — but 5↔3 bridge and U(1)→Y both undefined."

---

## What this audit does and does not claim

- **Does** DERIVE the linked-channel braid word `σ₁^{±2}` (Hopf link
  `T(2,±2)`) with provenance from `fermion-boson-knot-link.md` +
  `inter-nucleon-channel-color-tube.md` — not chosen to hit a target.
- **Does** compute the Markov trace symbolically in q + RAW @ 60 dps, with
  the `(2)`/`(1,1)` Wedderburn block decomposition; cross-validates
  `tr_M(σ₁²)` against the census Hopf closed form to 0.0 at 60 dps.
- **Does** confirm writhe pp=+2/nn=−2 (linking number ±1) and non-Brunnian.
- **Does** verify single-crossing Markov destabilization `tr_M(σ₁)=z` exactly
  (trace-invariant) — the channel escapes the Brunnian block.
- **Does** show the U(1)_framing is live (writhe ±2 ≠ 0, pp/nn asymmetric).
- **Does NOT** close the 5↔3 bridge (the channel is 2-strand, not 5→3).
- **Does NOT** derive a hypercharge from writhe (misses PDG by ~305× at c=1;
  no canonical writhe→Y map). m_n−m_p is a falsification reference only.
- **Does NOT** propose, fit, or tune any coupling, normalization, or h^k;
  does NOT wire to production; does NOT advance L2 numerically; does NOT
  discharge any Lean `sorry`. No LP/SDP solve appears (no dual emission
  required).

## Cross-references

- The census + the lead:
  [`2026-06-01-knot-operator-census-group-actions.md`](2026-06-01-knot-operator-census-group-actions.md)
  (PR #1677).
- The missing 5↔3 functor + U(1)=writhe + spin=ribbon-twist:
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
  (PR #1672),
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md)
  (PR #1670).
- The inter-nucleon channel (primary source for the braid word):
  [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md).
- Fermion/boson = knot/link, the 2-component link sector:
  [`fermion-boson-knot-link.md`](../../content/quantum-observable-universe/particle-interactions/fermion-boson-knot-link.md).
- Brunnian Borromean (the obstruction escaped):
  [`brunnian-property-of-borromean.md`](../../content/quantum-observable-universe/particle-interactions/brunnian-property-of-borromean.md).
- Markov (de)stabilization = vertical α_V:
  [`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md).
