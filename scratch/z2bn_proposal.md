# Proposal: Owner-Gated Geometric Derivation of Lever-1 Keystone (Bean z2bn)

## 1. Background & Current State
The algebraic investigation for Lever-1 (deriving/testing the fibre $q$-difference keystone) was fully concluded in Stages 6-9 (as of 2026-06-28). The explicit goal to "fit $D(m)$ to a single Habiro element, verify held-out $m$" yielded a sharp **negative** result in Stage 6: the binding correction tower is NOT a single low-order $q$-hypergeometric element (the literal contiguity template fails held-out falsification).

Through direct cyclotomic factorization (Stages 7-9), the complete real-$q$ algebraic structure of the correction $D(m)$ was mapped:
$$ D(m) = (q-1)^2 \times [\Phi_d \text{ tower with odd-d rule}] \times [R_m \text{ cores}] $$
The $R_m$ cores are pairwise-coprime, irreducible, bar-symmetric, substrate-positive generic polynomials with mixed root distributions (both on and off the unit circle). There is no finite special-function closed form.

## 2. The Blocked Step: Geometric Derivation
Because the algebraic structure is fully mapped without a finite cyclotomic or hypergeometric closed form, further algebraic probing has diminishing returns. 

The genuine **derivation** of the keystone is now strictly **OWNER-GATED**. The algebraic work has handed over a complete, exact, parameter-free target constraint. The remaining decisive step is the geometric $\lambda_{SW}$-holonomy derivation on the color $E_q$ curve (tr B side, PR #2722).

## 3. Proposed Action for the Author
To fully resolve bean `z2bn`, the author must execute the geometric derivation step:
- **Target:** Construct the explicit $q$-difference operator $R(q,x)$ whose $\oint \lambda_{SW}^{(n)}$ residues reproduce the known anchors ($1$, $(q+1)^2/(3q)$, and Family-A) using the abelianised $\lambda_{SW}$ real connection holonomy on the color $E_q$ curve.
- **Context:** Sage tooling is confirmed available in-container (mpmath 1.3.0 + sympy 1.14.0 are pip-installed). The color spectral curve $\Sigma$ and $\lambda_{SW} = X dz$ have already been validated (Step 1, PR #2755).
- **Next Step:** Proceed with the numerical/analytic elliptic-period integration to derive $\tau$ independent of the 2.6424 seed, coordinating with the geometric `tr B` sibling (#2722) to avoid duplicated effort.
