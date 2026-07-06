# The canonical spin→colour coupling is the Hopf moment map; the round-S⁵ colour Reeb is transverse to it

**Date:** 2026-06-16
**Branch:** `claude/s5so3-hopf-coupling-obstruction-2026-06-16`
**Status:** partial construction + verified obstruction on the dynamical coupling of `conj:s5-so3-fiber-action`.
**Discipline:** formalize-first — construct what is canonical, verify the obstruction, state the resolution
direction; no fit.

## Setup

After the merged #2352/#2361/#2364/#2367/#2368, the keystone's lone open object is the **dynamical**
spin–colour coupling: an $A_5$-equivariant intertwining of the spin Hopf Reeb flow ($S^3\subset\mathbb{C}^2_{\mathrm{spin}}$,
$2I$) with the colour Sasakian Reeb flow ($S^5\subset\mathbb{C}^3_{\mathrm{colour}}$, $A_5$ via $T_1$). The
Reeb-eigenvalue resonance route was refuted (negative probe). This note constructs the coupling **map** and
tests whether it intertwines the two Reeb flows.

## The canonical coupling map (CONSTRUCTED — `scripts/s5so3_ingredient4_hopf_coupling_obstruction.py`, exit 0)

The unique natural $A_5$-equivariant coupling is the **Hopf moment map**
$$
\mu:\mathbb{C}^2_{\mathrm{spin}}\longrightarrow \mathbb{R}^3\subset\mathbb{C}^3_{\mathrm{colour}},\qquad
\mu(z)=\big(z^\dagger\sigma_x z,\; z^\dagger\sigma_y z,\; z^\dagger\sigma_z z\big),
$$
i.e. the $\mathrm{Ad}:\mathrm{SU}(2)\twoheadrightarrow\mathrm{SO}(3)$ map at the vector level (equivalently the
Hopf fibration $S^3\to S^2$). Verified properties:

1. **Resolves the spin-parity obstruction.** $\mu$ is **quadratic**, so $\mu(-z)=\mu(z)$: the central $-1\in 2I$
   acts **trivially** on the image. The quadratic map bridges the *odd* spinor (central $-1\mapsto-1$) to the
   *even* colour real form $\mathbb{R}^3=T_1$ (central $+1$) — exactly the parity mismatch that blocked any
   *linear* $\mathbb{C}^2\to\mathbb{C}^3$ coupling. This is the geometric realization of the Schur-forced static
   coupling.
2. **Intertwines the spin Reeb.** $\mu(e^{i\theta}z)=\mu(z)$: the spin Hopf Reeb (the phase circle) is exactly
   the $\mu$-fibre — $\mu$ *is* the Hopf fibration, so the spin Reeb is intertwined (vertical) by construction.
3. **$A_5$-equivariant.** $\mu(gz)=\mathrm{Ad}(g)\,\mu(z)$ for $g\in\mathrm{SU}(2)$ (verified for a random $g$ and
   for an order-5 binary-icosahedral generator, $g_5^5=-I$). So $2I$ on $\mathbb{C}^2$ descends to $A_5\cong I$ on
   $\mathbb{R}^3$.

## The obstruction (VERIFIED)

4. **The round-$S^5$ colour Reeb is transverse to $\mu$'s image.** The colour Sasaki–Einstein Reeb is the overall
   $\mathrm{U}(1)$ phase $e^{i\phi}$ on $\mathbb{C}^3$. Acting on a real vector $\mu(z)\in\mathbb{R}^3$ it gives
   $e^{i\phi}\mu(z)$, which has nonzero imaginary part for generic $\phi$ — it **leaves** $\mathbb{R}^3$. So the
   colour Reeb does **not** preserve $\mu(S^3)=S^2\subset\mathbb{R}^3$, and $\mu$ intertwines the **spin** Reeb but
   **not** the round-$S^5$ **colour** Reeb. The two flows are transverse at the coupling locus.

The geometric reason is sharp: the icosahedral $A_5$ lives in the **spatial** $\mathrm{SO}(3)_{\mathrm{colour}}\subset\mathrm{SU}(3)$
(real rotations of $\mathbb{R}^3$), whereas the round colour Reeb is the **phase** $\mathrm{U}(1)\subset\mathrm{SU}(3)$ —
a *different* circle, transverse to the real form where the $A_5$/spin structure sits.

## Reframe — the obstruction is on the phase circles, NOT the generation selection

A further check (verified, step 5) shows the obstruction does **not** block the generation coupling, because the
spin Hopf Reeb is not the generation direction:

- **The spin Hopf Reeb (overall phase $e^{i\phi}I$) is $\mathrm{Ad}$-trivial** — it maps to the identity in
  $\mathrm{SO}(3)$ (and is not even in $\mathrm{SU}(2)$: $\det\ne1$). It is precisely the $\mu$-fibre, with **no
  spatial $\mathrm{SO}(3)$ image**.
- **Generation degree $\ell$ is a spatial datum.** $\ell$ is an $\mathrm{SO}(3)$ spherical-harmonic level on the
  *base* $S^2 = S^3/\mathrm{Hopf}$ — governed by the **spatial** $\mathrm{SO}(3)$ (the non-central rotations),
  not the phase.
- **$\mu$'s spatial $\mathrm{SO}(3)$-equivariance carries the selection.** Since $\mu(gz)=\mathrm{Ad}(g)\mu(z)$,
  the *same* $A_5\subset\mathrm{SO}(3)$ acts on the spin base $S^2$ and the colour $\mathbb{R}^3$ — so the
  generation **selection** $\ell\mapsto\lambda$ is already realized by $\mu$'s spatial equivariance (the
  $\ell$-harmonic and the $\lambda$-block share the same $A_5$-isotype, per the verified bridge + the Schur-forced
  static coupling).

So the transversality of step 4 is on the **contact phase circles** (spin Hopf phase / colour Sasakian phase),
which are orthogonal to the generation direction; **it does not block the $\ell\mapsto\lambda$ selection.** What
genuinely remains is the **Markov-trace weighting** — the contact/dynamical structure supplying the $y_\lambda$
weights — which is where the colour Reeb must sit in the spatial $\mathrm{SO}(3)_{\mathrm{colour}}$.

## Resolution direction (next construction target, open)

The coupling that intertwines both flows requires the **colour Reeb to lie in the spatial
$\mathrm{SO}(3)_{\mathrm{colour}}\subset\mathrm{SU}(3)$**, not the phase $\mathrm{U}(1)$. That is a contact
structure on an $\mathrm{SU}(3)/\mathrm{SO}(3)$-homogeneous space (the real flag / Wu-manifold family), **not** the
round $S^5$. Constructing that Sasakian structure and checking its Reeb intertwines the spin Hopf via $\mu$ is the
precise next step — owner-gated, multi-session.

## Net for `conj:s5-so3-fiber-action`

- **Coupling map:** constructed (Hopf moment map $\mu$) — resolves parity, realizes the static coupling,
  intertwines the spin Reeb. This is real geometric progress: the coupling is no longer "unknown", it is $\mu$.
- **Generation selection $\ell\mapsto\lambda$:** carried by $\mu$'s spatial $\mathrm{SO}(3)$-equivariance — the
  same $A_5\subset\mathrm{SO}(3)$ on both sides. So the *selection* part of the fibre map is realized.
- **Obstruction (phase circles only):** the *round-$S^5$* colour Reeb (phase) is transverse to $\mu$, but this is
  the contact direction, **not** the generation direction (the Hopf Reeb is Ad-trivial). It does not block the
  selection.
- **Remaining (open):** the **Markov-trace weighting** ($y_\lambda$) — the contact/dynamical structure, which
  requires the colour Reeb in the spatial $\mathrm{SO}(3)_{\mathrm{colour}}$ (an $\mathrm{SU}(3)/\mathrm{SO}(3)$-homogeneous
  Sasakian, not round $S^5$). That is the single concretely-posed construction left.
- No fit; the obstruction is a verified transversality, not a numerical near-miss.

## Cross-references

- [`2026-06-16-s5so3-two-sasakian-construction-attempt.md`](2026-06-16-s5so3-two-sasakian-construction-attempt.md) — the two Sasakian sides + static/dynamical split
- [`2026-06-16-s5so3-reeb-resonance-probe-negative.md`](2026-06-16-s5so3-reeb-resonance-probe-negative.md) — the refuted eigenvalue-resonance route
- `scripts/s5so3_ingredient4_hopf_coupling_obstruction.py` — this construction + obstruction (exit 0)
