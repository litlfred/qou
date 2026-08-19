# The (N, k) menu scan — result: 0/8, and the winding route is closed

**Date:** 2026-07-12 · **Axis:** c₃ bar-odd S geometric instantiation ·
**Executes:** [`2026-07-12-mq0-unified-boundary-selection.md`](2026-07-12-mq0-unified-boundary-selection.md) §5
(PR #3660). · **Result compute:**
[`qbeta_c3_mq0_nk_scan.py`](../../computations/qbeta/qbeta_c3_mq0_nk_scan.py) ·
**Tier:** scope-(a) numerical falsification; no fit, nothing wired.

## What was computed

The branch-tracked complex volume `𝔙(u) = Vol(u) + i·CS(u)` of the figure-eight
4₁, from Murakami–Yokota's theorem-grade formula (`library/arxiv-math-0401084v3/0401084v3.pdf`,
math/0401084, Thm 2.1/2.2):

- explicit shapes `z(u), w(u)` (radical form, √-branch fixed by continuity from
  `z=w=e^{iπ/3}` at `u=0`), cross-checked against the gluing equations to 1e−20;
- potential `Φ(u) = ∫₀^u 2v du'`, `v = 2 log(z(1−z))` continued along the ray
  (winding-robust), `f = (Φ − uv)/4`, `𝔙 = Vol(4₁) − 2πi·f`.

**Validated (5/5 assertions, full precision):** `u=0 ⇒ Re 𝔙 = Vol(4₁)`,
`Im 𝔙 = 0`; NZ leading slope `dv/du|₀ = 2√−3` (Hikami `2v = −2πi + 4√3 i u + …`);
Murakami gluing residual 1e−20; `Im 𝔙 = 0` on the real-u axis.

## Result: 0/8

Every named candidate `(N,k) ∈ {3,6,60,120} × {1,2}` fails, at every anchor:

| finding | value |
|---|---|
| least-bad candidate (N=120, k=2) | overshoots `\|S_proton\|` by **~40×** |
| six large-`\|Im\|` candidates | overshoot by **1e2–1e4×** |
| endpoint Bloch–Wigner volume `D(z)+D(w)` | negative or ≈0, **not** the geometric +2.03 |

The meridian data `u(N,k) = N·t − 2πi·k` have `|u| ≥ 2π ≈ 6.28`, which is far
outside Murakami's proven neighborhood of 0; the continuation leaves the 4₁
geometric component (the true hyperbolic volume is bounded by `Vol(4₁)=2.03`,
yet these endpoints give negative/≈0 Bloch–Wigner values on a non-geometric
sheet).

## The structural finding — the memo's G2 framing was backwards

The memo celebrated *"G2 passed automatically because `|u| ≥ 2π ≫ floor 0.2135`."*
That is a **misframing**. The G2 floor is the `|u|` at which the *available*
`|Im 𝔙| ≈ (√3/2)|u|²` first **reaches** `|S|`:

- `|u| ≈ 0.21` gives `Im 𝔙 ≈ |S| ≈ 0.04` — the intended match;
- `|u| ≥ 2π` gives `Im 𝔙 ≈ 34–270` — a **40–7000× overshoot**, not a pass.

So the winding form `u = N·t − 2πi·k` (`|u| ≥ 2π`) is **incompatible** with the
small `|u| ≈ 0.21` that S's magnitude demands. A viable meridian assignment
needs a tiny `|u|`; a real tiny `|u|` gives `Im 𝔙 = 0` (C1-dead). The honest
surviving direction from the meridian side is a **small-`|u|` complex
(phase-channel)** assignment — not the large-`|u|` winding lattice.

## Reconciliation — superseded by the merged Ohtsuki-tower resolution

While this menu was being scanned, `main` landed the **decisive** resolution of
the odd-S origin from the *quantization* side rather than the meridian side:

- The Ohtsuki tower `𝔙_b = 𝔙_0 + Σ κ_n (2πb²)ⁿ` (real `κ_n`) at the substrate
  **small imaginary** parameter `2πb² = i·t` (`|·| = t ≈ 0.10`) —
  [`rem:ohtsuki-tower-bar-parity`](../../content/quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md).
- A **Lean-proved bar-parity selection rule** (even rungs → real → Vol;
  odd rungs → imaginary → CS = S): `OhtsukiTowerBarParity.even_rung_real`,
  `.odd_rung_imaginary`.
- **Borel–Padé resummation** → smooth `Im 𝔙 ≈ 0.055`, action `A = Vol(4₁)/π`,
  no Stokes ambiguity (`qbeta_c3_borel_pade_resummation_probe.py`). The odd-S
  sign-flip is the `1/u³` ladder **representation** of that smooth object —
  representational / experimental-`Q_β`-limited, not a physical singularity.

This scan is the **complementary meridian-side negative**. The substrate's
leading odd rung `Im[κ₁·(2πb²)] = Im[κ₁·i·t] = 0.058` (`κ₁ = 11√3π/108`) lands
at the target **O(0.05)** — the small-parameter route is right; the large-`|u|`
winding route is a dead end. The memo's open `(N,k)` proposal is **closed**.

## Caveat (recorded)

Absolute `Im 𝔙` (CS) at `|u| ~ 6–18` is normalization-uncertain: the
branch-integral and the standard leading-NZ `(√3/2)|u|²sin2φ` disagree by
O(1)–O(100) because `|u|` is far outside the small-`|u|` regime where either is
controlled. The extended-Bloch flattening that would pin the absolute CS was
**not** computed — it does not change the verdict (both estimates overshoot by
≥40×; the Bloch–Wigner volumes are off-component regardless). What is validated
to full precision is listed above.

## Cross-references

- Memo / kit: [`2026-07-12-mq0-unified-boundary-selection.md`](2026-07-12-mq0-unified-boundary-selection.md),
  `QOU.QBeta.BarOddLadderShape` (PR #3660).
- Merged resolution: `rem:ohtsuki-tower-bar-parity`, `OhtsukiTowerBarParity.lean`,
  `qbeta_c3_borel_pade_resummation_probe.py` (PRs #3675-thread / merged 2026-07-12).
- Literature source: Murakami–Yokota, *The colored Jones polynomials of the
  figure-eight knot and its Dehn surgery spaces*, math/0401084.
