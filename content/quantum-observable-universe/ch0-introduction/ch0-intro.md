> *The enormous usefulness of mathematics in the natural sciences
> is something bordering on the mysterious and there is no rational
> explanation for it.*
> — Eugene Wigner, 1960 \cite{wigner1960}

> *What we observe is not nature itself but nature exposed to our
> method of questioning.*
> — Werner Heisenberg, 1958

This paper develops the **mechanics** of quantum observable
universes.  We do not say what the universe *is* — we say what
its mechanics *do*.  Category theory is the natural language
because it describes morphisms and structure — the *how* —
without committing to ontology, whether constructive or platonic.

We begin from what we can actually observe:

1. **Differentiation works.**  Linear approximation describes
   our universe across scales — from planetary orbits to
   particle scattering.  This motivates Kähler differentials
   as the algebraic substrate.

2. **Measurement is consistent.**  We can measure, record, and
   compare.  The Frobenius relation encodes this: a trace
   that pairs observables with their duals.

3. **Physics is frame-independent.**  What we measure does not
   depend on the orientation from which we observe it.  Three-
   dimensional rotation — $\mathrm{SU}_2(R)$, the double cover
   of the rotation group $\mathrm{SO}_3(R)$ — emerges via
   Tannaka–Krein reconstruction from the rigid monoidal
   structure.  We do not assume $\mathrm{SU}_2(R)$; it falls
   out of the axioms.

4. **Three-fold structure recurs.**  Three colours (red, green,
   blue), three-fold chirality, three generations of matter.
   The Bring's surface and its $S_5$ symmetry encode this
   preference for three.

5. **Time flows.**  The universe folds and unfolds; we drift
   along the flow.  The Reeb vector field provides the clock.
   Lifting and descent through the jet tower give the
   direction.

6. **We share a local patch.**  We can discuss events with
   each other, compare measurements, and agree on outcomes —
   at least locally.  This is the descent condition: local
   data extend to a shared global structure.

7. **Measurement is never exact.**  There is always
   uncertainty — not randomness, but the signature of a
   geometric degree of freedom we have not resolved.  The
   Reeb bundle --- the $U(1)$ fibration over the exceptional
   divisor --- is where we keep track of what we have not
   yet measured.

8. **We have the perception of free will and intent.**
   We choose to measure, to act, to organise.  Choosing to
   sort a sock drawer is an act of intent that increases
   local order at the cost of effort.  The mathematical
   consequence: observation is an **open map** — it creates
   outcomes not determined by the initial conditions.

9. **Multiple observers share a world.**  This is not a
   flashlight theory where each observer illuminates a
   private universe.  Each fibre functor
   $\tau \colon \mathbf{C} \to \mathbf{Vect}$ is an
   affine chart — one observer's local coordinate system.
   Different fibre functors are different charts;
   Tannaka–Krein tells us that the natural isomorphisms
   between them form a $G$-torsor — the transition
   functions.  The cocycle condition is automatic:
   functoriality forces chart overlaps to be consistent.
   The affine atlas is not an extra assumption; it is a
   consequence of the rigid monoidal structure
   ([contact affine chart](#def:contact-affine-chart)).

These observations motivate a rigid monoidal category — a
quantum observable universe — whose axioms encode precisely
these features and nothing more.

**[Chapters 1–2](#chap:qu)** build the categorical framework:
rigid monoidal categories, fibre functors, Frobenius structure,
dagger involution, Tannaka–Krein reconstruction of
$\mathrm{SU}_2(R)$, the categorical action $S_q$, and the three
variational equations (Einstein, Yang–Mills, transport).

**[Chapter 3](#chap:torsion)** establishes lifting and descent:
the obstructions to extending local data to global structures,
and the descent involution $\hat{\tau}$ that decomposes the
algebra into descended (observable) and transient (pre-observable)
modes.

**[Chapter 4](#chap:path-integrals-braiding)** develops braids
and knots.  The Hecke algebra provides crossing coefficients,
the Markov trace computes Skein polynomials, and crossing number
equals jet order equals information content.

**[Chapters 5–6](#chap:models-qou)** construct explicit models.
We call it a *Descartes universe* because the observer is not
separate from the mechanics — we think about the world, but we
are part of it.  The Archimedean condition and the Euler
characteristic $\chi = -6$ are driven by physical observation,
formalised mathematically here and compared to measurement in
[Chapter 7](#chap:observations).  Bring's surface, the nuclear
Skein polynomial $P_{\mathcal{N}}(q)$, and the universal beta
decay matrix $\Delta_\beta(q)$ are constructed explicitly.

**[Chapter 7](#chap:observations)** presents experimental
evidence: the skein-theoretic mass formula and comparison with
measured hadronic spectra.

**[Chapter 8](#chap:info-theory)** addresses Wigner's mystery.
The mechanics of the QOU are **Turing complete**: the Toffoli
braid amplitude $P_{7,6}(q) \neq 0$ for all $q \neq 1$, so
any computable function can be executed as braid crossings at
discrete Planck steps.  The universe supports logic and
computation in all forms — from pebbles to microchips — because
the combinatorics is a property of the substrate parameter, not
the medium.  This chapter does not answer whether mathematics
is discovered or invented.  It tells us we do not have to.

**[Chapter 9](#chap:organic-chemistry)** applies the Hopf chain
formalism to organic chemistry.

The **Glossary** maps paper terminology to Mathlib declarations.
The **Appendix** collects the knot periodic table.
