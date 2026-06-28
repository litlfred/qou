The conjecture that per-irrep character differences factor via
$\Phi_{4 f_\lambda}(q)$ — with $d_\lambda = 4 f_\lambda$ tied to the
SYT count $f_\lambda = n!/H(\lambda)$ — is stated and Lean-verified at
$n = 3$ in [`conj:phi-d-syt-count`](#conj:phi-d-syt-count), building on
the closed-form data of
[`rem:chi-per-irrep-cyclotomic-closed-forms`](#rem:chi-per-irrep-cyclotomic-closed-forms).
This remark interprets that conjecture: what it would buy the
categorical-chain derivation, and which literature it connects to.

## Significance

If the conjecture holds at all $n$, it provides a **structural
prediction** for the per-irrep contribution to $\tau_M$ as a function
of purely combinatorial partition data ($f_\lambda$, $H(\lambda)$, $c(\lambda)$).
Combined with the Wenzl-bridge $y_\lambda$ weights and the
precision-ladder $c_k$ extraction, this would close the categorical-
chain derivation **at every order** for arbitrary multi-baryon
typed braids:

- B_3 $\to$ c_k for proton/neutron (current)
- B_6 $\to$ c_k for di-baryon (deuteron) systems
- B_9 $\to$ c_k for tritium / He-3
- B_12 $\to$ c_k for α-particle (${}^{4}$He)

The cyclotomic structure also opens a **literature bridge** to
Ariki-Koike cyclotomic Hecke algebras (Mathas 1999), where Specht
modules decompose along $\Phi_d(q)$ factors at the
parameter-cyclotomic structure.
