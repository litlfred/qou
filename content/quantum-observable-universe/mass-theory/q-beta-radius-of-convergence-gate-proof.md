## Proof sketch

**Forward direction** (the proved part): The pinned $c_k$ values
$c_2, \ldots, c_{10}$ from the canonical SDP extraction
(`qbeta-decay-sdp-extended-ck.witness.json`) satisfy
$c_k \cdot u_{\text{substrate}}^k \to 2.118 \times 10^{-13}$ for $k = 8, 9, 10$
with **0.02 % spread** (asymptotic constancy). This is the signature of a
simple pole: if $g(u) \sim A \cdot u_{\text{subst}} / (u_{\text{subst}} - u)$
near $u = u_{\text{substrate}}$, expanding gives
$c_k \sim A / u_{\text{subst}}^{k-1}$, so $c_k \cdot u_{\text{subst}}^k \to A$.
A branch-fit on $\log(c_k u^k) \sim (\beta - 1)\log k$ gives $\beta = 0.999$
($\beta = 1$ IS the simple-pole case), and the essential-singularity
hypothesis is ruled out by the flat asymptote.

**Gate direction** (this proposition, the new content): If a candidate
Habiro element $F(q)$ generates ladder coefficients $\tilde c_k$ via the
$\S 3b$-cond conditional class pattern (the `CFinite.recurrence_step` engine),
then the rational-function singularity locator on $\tilde g(u) = \sum \tilde c_k u^k$
extracts the candidate's nearest pole $u_0$. If
$|u_0 - u_{\text{substrate}}| / u_{\text{substrate}} > 10^{-6}$ (fibre-level
tolerance from the cross-anchor bound), the candidate fails the gate. $\blacksquare$

## canonical anchor (verified)

From the canonical SDP extraction at $q_0 = 1.10997858\ldots$:

| quantity | value |
|---|---|
| $u_{\text{substrate}}$ at $q_{\text{proton}}$ | $0.008517234550156142$ |
| $u_{\text{substrate}}$ at $q_{\text{muon}}$ | $0.008517236340043958$ |
| relative shift | $2.10 \times 10^{-7}$ (210 ppb) |
| asymptotic $c_k \cdot u^k$ ($k \in \{8,9,10\}$) | $2.118 \times 10^{-13}$ |
| spread | $0.02$ % |
| branch-fit $\beta$ | $0.999$ (simple-pole case is $\beta = 1$) |
| ratio test $c_{k+1}/c_k$ at $k = 10$ | $\to 1 / u_{\text{substrate}} = 117.4$ |
