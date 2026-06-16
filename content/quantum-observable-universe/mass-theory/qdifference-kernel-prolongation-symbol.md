**Conjecture (the q-difference kernel is the prolongation symbol).**

The $q$-difference kernel $R(q,x)$ of the binding generating function
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)) **is
the symbol of the jet-prolongation operator** $J^{n}E\to J^{n+1}E$ of the
Seiberg--Witten connection
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)) — equivalently, the
monodromy/Stokes data of the prolonged SW connection at the branch-point poles
of $\lambda_{\mathrm{SW}}^{(n)}$ on $\mathcal{S}_c\cong\mathbb{P}^1$.

Two consequences follow:

1. **$R$ is structurally fixed, not fitted.** The prolongation operator is a
   single fibre-level object; its symbol is read off the connection, not
   tuned to reproduce the terms. This is forced by the precision-floor
   obstruction (the $c_k$ information bound makes term data unable to fix $R$
   beyond low order), and it is the same fibre-level / root-of-unity
   singularity structure that governs the $\mathfrak{Q}_\beta$ ladder.
2. **It closes the binding program.** Given $R$, the recurrence of
   [`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)
   determines every body term from the deuteron base case (fixing the
   $\rho\cdot A$ growth law), which is precisely the per-term mass identity
   (B). Feeding (B) into
   [`thm:binding-closure-conditional`](#thm:binding-closure-conditional)
   discharges its one conditional input, promoting
   [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)
   from conditional to unconditional.

This conjecture is therefore the **single keystone** of the step-9b binding
closure: the residue form (D), the body-order = jet-degree coincidence (C), and
the recurrence machinery (L3) are all proved; only the identification of $R$
with the prolongation symbol remains. It is stated here as a precise,
falsifiable structural claim — to be *derived* from the prolonged connection's
local monodromy, not searched numerically.
