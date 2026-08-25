# Draft note to R. van der Veen — three corrections to *Proof of the volume conjecture for Whitehead chains*, and an evaluation of `E`

**Status: DRAFT, NOT SENT.** Sending is an outward-facing action to a named
person and is the repository owner's call, not the agent's. Bean `qou-vdvE`.

**Subject paper.** R. van der Veen, *Proof of the volume conjecture for
Whitehead chains*, Algebr. Geom. Topol. **8** (2008) 603–624; arXiv:math/0611181.
Local copy `library/arxiv-math-0611181v2/0611181v2.pdf`.

**Reproducibility.** Every numerical claim below is produced by
`computations/probes/one_loop_vdv_constant_closed_form_probe.py` in this
repository, which computes `Q_N` directly from the paper's Lemma 1 and compares
it against closed forms stated in advance. Nothing is fitted.

---

## Summary

Your main theorem is unaffected by everything below. It needs `Vol`, `D`, and
`E ≠ 0`, and all three survive. The corrections bear only on the constant `E` —
the quantity your closing paragraph defers, citing the Gukov–Murakami conjecture
that it is determined by the Ray–Singer torsion.

That constant now has a closed form for the whole `b = 1` family. Writing
`n := c+d` and `m := 4a − c + d`:

```
Q_∞ = exp( iπ(4a+3c−3d)/4 ) · 2^{−n/2} · √(2/A),      A := n − m i

Re E = 2π[ (1/2 − n)·log 2 − ¼·log(n² + m²) ]
Im E = π·arctan(m/n) + π²(4a+3c−3d)/2
```

Reaching it required correcting three things in the published proof, listed
below with the check that detects each.

---

## 1. Lemma 2a is stated in distances where the Taylor expansion is signed

Lemma 2a defines `n′ = |n − ⌊N/2⌋|` and `k′ = |k − ⌊N/4⌋|` and asserts

```
S_{n,k}·S̃_N^{−1} = exp(−(π/N)(n′² + 2n′k′ + 2k′²)) + O(N^{3δ−2}).
```

The Taylor expansion this comes from, in the proof of Lemma 2,

```
f(π/2 + x, π/4 + y) = f(π/2, π/4) − (x² + 2xy + 2y²) + O(|x|³+|y|³),
```

is signed, and the cross term `2xy` is negative when `x` and `y` have opposite
signs. Evaluating `log(S_{n,k}/S̃_N)` directly from Lemma 1 at `N = 4000`, on the
corner `n′ > 0, k′ < 0`:

| `n′` | `k′` | true | signed form | Lemma 2a as printed |
|---:|---:|---:|---:|---:|
| 10 | −10 | −0.070920 | −0.078540 | −0.392699 |
| 20 | −20 | −0.300637 | −0.314159 | −1.570796 |
| 30 | −15 | −0.353311 | −0.353429 | −1.767146 |
| 15 | −30 | −0.857281 | −0.883573 | −2.297290 |
| 40 | −25 | −0.660549 | −0.667588 | −3.809181 |

The quadratic form `x² + 2xy + 2y² = (x+y)² + y²` is positive definite either
way, so `Q_∞ ≠ 0` and the volume conjecture is untouched. But the absolute
values are what turn the Step-4 Gaussian into an integral over an orthant, and
hence what produce the `erfc` factors in Step 6. With the signs restored the
integral runs over all of `ℝ^{n+1}` and is a plain Gaussian:

```
Q_∞ = ψ ∫_{ℝ^{n+1}} exp(−π[ A u²/2 + 2 Σⱼ (vⱼ + u/2)² ]) du dv
    = ψ · 2^{−n/2} · √(2/A)
```

the `v`-integrals being complete Gaussians equal to `2^{−1/2}` independently of
`u`. This is elementary for **every** `n`, not only for small `n`.

## 2. The expression `4a + c − d` should be `4a − c + d`

It occurs in two places.

**(a) Step 3 of the proof of Lemma 4** defines the Gaussian coefficient
`A = (c+d) − (4a+c−d)i`. The `χ`-exponent supplied by Lemma 1 is `4a − c + d`,
and that is what the asymptotics return. Of 20 chains swept, the six with
`|4a+c−d| ≠ |4a−c+d|` discriminate between the two readings, and all six agree
with `4a − c + d`. Sample (`|Q_∞|`, Richardson-extrapolated from `N = 1600, 3200`
against the closed form):

| `(a,c,d)` | measured `\|Q_∞\|` | `A` with `4a−c+d` | rel. err |
|---|---:|---:|---:|
| `(1,1,0)` | 0.562341171 | 0.562341325 | 2.7e−07 |
| `(1,2,1)` | 0.242745242 | 0.242745886 | 2.7e−06 |
| `(1,0,2)` | 0.281170374 | 0.281170663 | 1.0e−06 |

**(b) The main theorem's `CS`.** As printed, `CS = −(4a+c−d)/8·2π²` when
`c+d = 1` and `−(4a−7c+7d)/8·2π²` otherwise. Measuring the `N`-linear phase
directly — `arg(R_{N+1}/R_N) → −qπ/8` where `CS = −(q/8)·2π²`, and `R_N :=
J_N N^{−(n+3)/2} S̃_N^{−n}` — gives (compared mod 16, since the phase is
`e^{−iqπN/8}`):

| chain | `q` measured | this note | as printed |
|---|---:|---:|---:|
| `W_{0,1,1,0}` | −1.00001 | −1 | **+1** |
| `W_{0,1,0,1}` | +1.00001 | +1 | **−1** |
| `W_{1,1,1,0}` | 2.99999 | 3 | **5** |
| `W_{0,1,2,0}` | −2.00000 | 14 ≡ −2 | **−14 ≡ 2** |
| `W_{0,1,2,1}` | 7.00000 | 7 | **−7** |
| `W_{0,1,3,0}` | 5.00000 | 21 ≡ 5 | **−21 ≡ 11** |
| `W_{1,1,0,2}` | 6.00000 | −10 ≡ 6 | **18 ≡ 2** |

so `q = 4a − c + d` at `c+d = 1` and `q = 4a + 7c − 7d` at `c+d ≥ 2` — the same
sign on `(c−d)` flipped in both branches. The branch difference is only `φ_N`,
which is defined differently in the two cases and contributes a linear phase
`−8(c−d)` in the second.

We note that the proof of Lemma 4 itself uses `e^{(4a+7c−7d)Nπi/8}` in its
definition of `Q_N`, i.e. the value this note arrives at, so `Q_∞` is
well defined as written and only the main theorem's statement is affected.

## 3. The `b ≥ 2` constant has the wrong sign on its real part

The main theorem gives, for `b ≥ 2` and odd `N`,
`E = 2π(c+d)log 2 + ((4a+3c−3d)/4)·2π²i`.

Lemma 5 gives the constant as `exp(−(c+d)log√2 + (4a+3c−3d)πi/4)`, which with
`S̃_N^{c+d} = e^{\mathrm{Vol}N/2π}(2N)^{−(c+d)/2}` yields
`|J_N| ∼ 2^{−(c+d)}N^b e^{\mathrm{Vol}N/2π}`, i.e. `Re E = −2π(c+d)log 2`.
Computing `|J_N|·N^{−b}·e^{−\mathrm{Vol}N/2π}` from Lemma 1:

| chain | limit | `2^{−(c+d)}` | `2^{+(c+d)}` |
|---|---:|---:|---:|
| `W_{0,2,1,0}` | 0.500000009 | 0.5 | 2 |
| `W_{0,2,1,1}` | 0.250000006 | 0.25 | 4 |
| `W_{0,3,2,0}` | 0.250000006 | 0.25 | 4 |

Lemma 5 is right; the transcription into the main theorem is not. The imaginary
part is correct, and it independently corroborates the phase of `Q_∞` in §4
below.

## A remark on Lemma 3, which is correct

The displayed expansion inside the proof of Lemma 3,
`s_n = (N/π)Λ(nπ/N) − ½log(n·sin(rπ)/(rπ)) + O(N^{−1})`, appears to have lost
the `−½log 2π` Stirling term that the preceding line supplies; the correct
expansion is `s_n = (N/π)Λ(nπ/N) − ½log(2N sin(rπ)) + O(N^{−1})`. This does not
affect Lemma 3: in the combination
`log S̃_N = −2s_{⌊N/4⌋+⌊N/2⌋} + 2s_{⌊N/4⌋} + s_{⌊N/2⌋}` the two extreme terms
cancel the discrepancy, and the stated
`S̃_N ∼ exp((4N/π)Λ(π/4) − ½log 2N)` is confirmed numerically
(`log S̃_N − 4NΛ(π/4)/π + ½log N → −½log 2 = −0.34657359`, from
`−0.34919157` at `N = 400` to `−0.34673721` at `N = 6400`).

## 4. The resulting evaluation of `E`

With §1 and §2(a) applied, `Q_∞ = ψ·2^{−n/2}·√(2/A)` with
`A = n − mi`, `n = c+d`, `m = 4a−c+d`. Against `Q_N` computed directly from
Lemma 1 on 20 chains spanning `c+d ∈ {1,…,4}` and `a ∈ {0,…,3}`: no mismatch,
worst relative error `5.0e−06`, the residual being the `O(1/N²)` Richardson
remainder and growing smoothly with `c+d`.

The phase is `ψ = exp(+i(4a+3c−3d)π/4)`, measured at `N ≡ 0 (mod 16)` where the
`CS` factor is exactly `1` so no convention enters: over 12 chains the error
against that sign is `4e−07` to `1.1e−06` and falls as `O(1/N)`, against the
opposite sign `0.34` to `1.19` on the nine chains where the two differ. It
agrees with the imaginary part of your own `b ≥ 2` constant.

Hence

```
c_σ := lim_N |J_N| N^{−3/2} e^{−Vol·N/2π} = 2^{1/2−n}·(n² + m²)^{−1/4}.
```

## 5. A consequence you may find interesting

Your closing paragraph records the Gukov–Murakami conjecture that `E` is
determined by the Ray–Singer torsion, and defers it. If one writes the
Dimofte–Garoufalidis 1-loop invariant `τ` and posits `c_σ = 2^{−1/2}|τ|^{−1/2}`,
the closed form above forces

```
|τ_DG|(W_{a,1,c,d}) = 2^{2n−2}·√(n² + m²),
```

so `τ²` is `16^{n−1}` times the norm of the Gaussian integer `n − mi`. We stated
this before locating the manifolds, then computed `τ` independently in SnapPy: it
is exact at the Whitehead link (`√2`) and the Borromean rings (`8`), and matched
to 18 digits at `L8n5` (`8√2`), `L10n100` (`16√10`) and `L10n103` (`48√2`),
which we identified afterwards as `W_{0,1,2,0}`, `W_{0,1,2,1}` and `W_{0,1,3,0}`
by volume and cusp number. The `a`-dependence — which enters your Lemma 1 only
through the phase `χ^{4a−c+d}` — was checked separately by reframing the `a = 0`
complement with meridian `μ − aλ`, since `Vol` is independent of `a`: 25
framings, no mismatch.

---

*Prepared with the assistance of an AI system; every numerical statement is
reproducible from the probe cited at the top, and the repository owner has
reviewed this note before sending.*
