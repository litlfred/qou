# f-map action A ≈ 0.69 (real, not a clean constant) + hexagonal-angle prune

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (action pin) · **Tier:**
structural-exact (Vol recovery, prune) + numerical (action, order-limited)
· **Discipline:** no fit, no c_k value, no wiring, no tier change. Follow-up to
#3482 (action real, amphichiral) / #3487 (Hopf cubic complex roots).

Probe [`qbeta_action_pin_refine.py`](scripts/qbeta_action_pin_refine.py) (5/5).

## Part A — the resurgence action A is real ≈ 0.69, but not a clean constant

Extending the 4₁ Ohtsuki ladder to **order 13** (dps 260, Vol recovered to
`2×10⁻³¹`), the large-order ratios `A_k = k·κ_{k-1}/κ_k` decrease smoothly through
the reliable window (`0.826, 0.811, 0.774, 0.750, 0.735, 0.725, 0.717, 0.711,
0.696`), and Aitken-Δ² acceleration gives **A ≈ 0.688**.

| candidate | value | rel to A |
|---|---|---|
| Vol/π | 0.6461 | **6.4 %** |
| 2/e | 0.7358 | 6.5 % |
| Vol/e | 0.7468 | 7.9 % |
| Vol/4 = Λ(π/3) | 0.5075 | 36 % |

**No framework constant sits within 1 % of A.** The action is a genuine real
categorical invariant of the even/amphichiral (4₁) sector (its reality is forced
by `CS(4₁)=0`, #3482), but **it does not reduce to a simple Vol-ratio at reachable
order**. The `A_k` are still slowly decreasing at k=11 (0.696), so `A_∞` may sit a
little below 0.69 (nearer Vol/π), but the numerical fit cannot pin it. The route to
a **closed form** is the exact saddle-point expansion of the Kashaev sum (rationals
over ℚ(√-3)), not a higher-order numerical fit.

## Part B — the complex-q ≈29° "hexagonal" thread is pruned

The Hopf-cubic complex root (#3487), mapped via `y = q²+q⁻²` back to a complex
substrate `q ≈ 1.036 − 0.577i`, has `|arg(q)| = 29.10°`. This is a **near-miss of
the hexagonal `π/6 = 30°`** (the ζ₃ angle) but **~3 % off, not equal** to it. So it
is **not** a hexagonal/ζ₃ angle — it is a generic algebraic angle of the **prime-19
cubic field** (disc −76), which is arithmetically distinct from the even channel's
`ℚ(√3)/ζ₃`. Pruned as numerology (scope-(a)); the odd channel's arithmetic
fingerprint stays prime 19.

## Net

Both threads resolve honestly: the action is real ≈0.69 but **not** a clean
framework constant (exact-saddle expansion needed), and the complex-q angle is
**not** hexagonal (prime-19 cubic, distinct arithmetic). Neither is a closure; both
sharpen the map and eliminate a tempting numerology. The one irreducible open
object remains S (CAL-2 = Subgoal-2), unchanged.

## Cross-references

- Probe: [`qbeta_action_pin_refine.py`](scripts/qbeta_action_pin_refine.py)
- Action real/amphichiral (#3482): [`2026-07-07-borel-pade-action-real-amphichiral.md`](2026-07-07-borel-pade-action-real-amphichiral.md)
- Hopf cubic complex roots: [`2026-07-07-parity-chirality-dictionary-closed.md`](2026-07-07-parity-chirality-dictionary-closed.md) (#3487)
