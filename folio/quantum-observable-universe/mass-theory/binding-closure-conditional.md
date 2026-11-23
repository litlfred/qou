**Theorem (binding closure, conditional on the inputs (C) and (B)).**

Suppose the per-isotope binding of the canonical braid $\mathcal{B}_K$ admits
the two structural inputs of the many-body conjecture ([Binding many-body series equals the jet-order filtration](#conj:binding-manybody-eq-jet-filtration)):

1. **(C)** the binding is the body-order series — the cluster
   filtration coincides with the jet-graded filtration
   ([Body order equals jet degree: the n-nucleon cluster sits at jet vertical degree n](#conj:bond-order-eq-jet-degree)):
   $B(K)=\sum_{n}\,(\text{$n$-body term})$; and
2. **(B)** each body term is $m_e$ times the corresponding
   prolonged Seiberg--Witten period, $B_n = m_e\,a_D^{(n)}$ (the mass
   identity applied to the degree-$n$ graded piece).

Then the binding has the closed form

$$
B(K) \;=\; m_e\sum_{n} a_D^{(n)}
\;=\; m_e\,2\pi i\sum_{n}\!\!\sum_{p\in\mathcal{S}_c^{\mathrm{hyp}}}\!\!
        \mathrm{Res}_p\,\lambda_{\mathrm{SW}}^{(n)},
$$

where the second equality is the residue form
([The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum), proved) and the
growth law is fixed by the $q$-difference recurrence
([The binding generating function's q-difference equation gives a depth-d recurrence](#prop:binding-genfun-qdifference)).

This is a **rigorous-conditional** result: it is proved modulo two named
inputs taken as hypotheses. Input (C), the grading coincidence, is
[a conjecture](#conj:bond-order-eq-jet-degree): its argument reads the
normal-form length through the conjectural jet-prefix order. Input (B), the
per-term mass identity, is open; it is equivalent to the existence of the
$q$-difference kernel $R$ realising the prolongation symbol. The residue form
is the residue theorem, $\oint_\gamma = 2\pi i \sum_{p \in E}
\mathrm{Res}_p$; which poles $E$ the period encloses is not settled there.
When (C) and (B) are derived, this theorem promotes the many-body conjecture to
an unconditional identity.

While the formal proof utilizes a standard conditional factor-out strategy over a finite set, packaging the multi-body sum structure through this specific closure mechanism to capture the Seiberg-Witten periods establishes a mathematically novel structural abstraction within the Quantum Observable Universe.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
