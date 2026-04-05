The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz))
depends on three levels of mathematical content.
This remark separates what is proved from what is genuinely
open.

### Level 1 — Algebra (proved)

The algebraic identity $[2]_q^2 - [3]_q = q$ and its
consequence $\lambda_q(1/2) = \sqrt{[3]_q/[2]_q^2} < 1$
are proved in Lean (`qInt_gap`, `reeb_averaged_contraction`).
This says: **if** an orbit spends equal time in $A_H$ and
$A_V$, it contracts.

### Level 2 — Bare Reeb equidistribution (established)

The Weyl equidistribution theorem
([Reeb equidistribution](#prop:reeb-equidistribution))
shows that the bare Reeb flow (without the Collatz
endomorphism) equidistributes phases on $[0, 2\pi)$
whenever $q \notin \mu_\infty$.  This gives
$\langle f_+ \rangle_{\mathrm{Reeb}} = 1/2$ for the
pure rotation.

The connection to torsion avoidance is direct: the Reeb
holonomy $e^{2\pi i/[2]_q}$ has irrational rotation
number for $q \notin \mu_\infty$, and Weyl's theorem
converts irrationality to equidistribution.

### Level 3 — The Collatz-Reeb cocycle (the genuine gap)

The $q$-Collatz orbit is **not** the bare Reeb flow.
It alternates the Hecke--Collatz endomorphism
$\widetilde{C}_q$ with the Reeb advance $\phi^q_{t_P}$:

$$
  a \;\mapsto\; \phi^q_{t_P}\bigl(\widetilde{C}_q(a)\bigr)
  \;\mapsto\; \phi^q_{t_P}\bigl(\widetilde{C}_q(\cdots)\bigr)
  \;\mapsto\; \cdots
$$

This is a **linear cocycle** over the Reeb rotation:
at each step, the Reeb flow rotates by angle
$\theta = 2\pi\alpha(q)$, and the Hecke--Collatz
endomorphism stretches/contracts in the rotated frame.
The orbit's Lyapunov exponent depends on the interaction
between rotation and stretch.

**What Level 2 gives:** The bare rotation equidistributes
phases, so $\langle f_+ \rangle_{\text{bare}} = 1/2$.

**What Level 3 needs:** The Hecke--Collatz perturbation
does not destroy equidistribution.  Formally: the
time-averaged fraction for the composite dynamics
satisfies

$$
  \langle f_+ \rangle_{\text{Collatz-Reeb}}
  \;\geq\; f_+^*(q)
  \;\approx\; 0.37,
$$

where the average is over orbits of
$\phi^q_{t_P} \circ \widetilde{C}_q$, not of
$\phi^q_{t_P}$ alone.

**Why this is non-trivial.**
The endomorphism $\widetilde{C}_q$ contracts the
$A_H$-component by $1/[2]_q$ and expands the
$A_V$-component by $[3]_q/[2]_q$.  After each step,
the element's "energy" is redistributed:

$$
  \|a_V\|^2 / \|a\|^2
  \;\xrightarrow{\;\widetilde{C}_q\;}
  \;\frac{([3]_q/[2]_q)^2 \,\|a_V\|^2}
         {(1/[2]_q)^2\,\|a_H\|^2 + ([3]_q/[2]_q)^2\,\|a_V\|^2}.
$$

If $\|a_V\| \gg \|a_H\|$, the Collatz step drives
$f_+$ toward $0$ — the element becomes "more odd."
The Reeb rotation then redistributes this, but whether
$\langle f_+ \rangle$ stays above $f_+^*$ depends on
**how fast the rotation mixes relative to the expansion**.

**The three possible regimes:**

| Regime | Condition | Collatz orbit |
|--------|-----------|--------------|
| Rapid mixing | Reeb rotation $\gg$ Collatz expansion | $\langle f_+ \rangle \approx 1/2$; converges |
| Critical | Reeb rotation $\sim$ Collatz expansion | $\langle f_+ \rangle = f_+^*$; Collatz horizon |
| Slow mixing | Reeb rotation $\ll$ Collatz expansion | $\langle f_+ \rangle < f_+^*$; diverges |

**What determines the regime:**
The Reeb rotation per step is $\theta = 2\pi / [2]_q$
and the expansion ratio is $[3]_q / [2]_q$.  The
competition is between the **mixing rate**
$\sin^2(\theta/2) = \sin^2(\pi/[2]_q)$ (fraction of
$A_V$-energy transferred to $A_H$ per rotation) and
the **expansion rate** $([3]_q/[2]_q)^2 - 1$.

At the QOU substrate value $q_0 \approx 1.1097$:
- Rotation angle: $\theta \approx 2\pi/2.11 \approx 2.98$ rad
- Mixing rate: $\sin^2(\pi/2.11) \approx 0.997$
- Expansion rate: $(1.584)^2 - 1 \approx 1.51$

The mixing rate ($0.997$) is comparable to but
below the expansion rate ($1.51$).  Whether the
orbit converges depends on the detailed interplay
— this is the genuine gap.

**Relation to existing theory.**
The Collatz-Reeb cocycle is a quasiperiodic linear
cocycle over an irrational rotation.  The theory of
such cocycles (Furstenberg, Herman, Avila) provides
tools:

1. **Furstenberg's theorem**: for i.i.d. random
   matrices, the Lyapunov exponent is determined by
   the average.  The Reeb rotation is deterministic
   (not random), but for Diophantine rotation numbers
   the orbit behaves "pseudo-randomly."

2. **Herman's subharmonicity**: for
   $\mathrm{SL}(2,\mathbb{R})$ cocycles over irrational
   rotation, the Lyapunov exponent is $\geq 0$.
   This does not immediately help (we need $< 0$
   for contraction).

3. **Avila's global theory**: for one-frequency
   analytic cocycles, the Lyapunov exponent is either
   $0$ (subcritical, $\langle f_+ \rangle > f_+^*$)
   or positive (supercritical).  The transition
   between regimes is sharp.

The $q$-Collatz conjecture asserts the cocycle is
**subcritical** (Lyapunov exponent $< 0$) — the Reeb
mixing overwhelms the Hecke expansion.  The $13\%$
excess of $1/2$ over $f_+^* \approx 0.37$ provides
the margin, but proving this for the composite
dynamics (not just the bare rotation) requires
analyzing the Collatz-Reeb cocycle as an analytic
cocycle over the irrational rotation $\alpha(q)$.

**The KAM connection.**
The paper notes that $q$-torsion leaves require
"KAM-type persistence results" when $q > 1$ breaks
periodicity.  The same KAM machinery applies here:
the Collatz endomorphism $\widetilde{C}_q$ is a
perturbation of the identity on $A$, and the
equidistribution of the bare Reeb flow persists
under small perturbations by KAM theory — provided
the rotation number $\alpha(q)$ satisfies a
Diophantine condition.  The torsion avoidance axiom
$q \notin \mu_\infty$ is necessary but may not be
sufficient; a Diophantine condition on $\alpha(q)$
would give a stronger (but more restrictive) result.
