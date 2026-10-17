---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-004-23-the-key-results
section_title: "The key results"
section_number: 2.3
pages: 10-13
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.856
latex_coverage_ratio: 0.859
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
Here we state and prove the key results relating ([\[h1\]](#h1){reference-type="ref" reference="h1"}), ([\[h8\]](#h8){reference-type="ref" reference="h8"}), ([\[h2\]](#h2){reference-type="ref" reference="h2"})--([\[h7\]](#h7){reference-type="ref" reference="h7"}), ([\[h9\]](#h9){reference-type="ref" reference="h9"}) and ([\[h10\]](#h10){reference-type="ref" reference="h10"}) to finite polynomial sums at roots of unity. We have chosen to present these results following the order in which the Bailey pairs in Section [\[arseBP\]](#arseBP){reference-type="ref" reference="arseBP"} were introduced.

::: theorem
[]{#Baileyfamily1 label="Baileyfamily1"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP1\]](#BP1){reference-type="eqref" reference="BP1"}. Then for $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily1eq}
        H_p^{(6)}(q) = \sum_{k=0}^{N-1} (-1)^k q^{\binom{k+1}{2} +(p-1)(k^2+k)} \alpha_k.$$
:::

::: theorem
[]{#Baileyfamily2 label="Baileyfamily2"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP2\]](#BP2){reference-type="eqref" reference="BP2"}. Then for $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily2eq}
        H_p^{(7)}(q)  = q\sum_{k=0}^{N-1} (-1)^k q^{\binom{k+1}{2} +(p-1)(k^2+k)} \alpha_k.$$
:::

::: theorem
[]{#Baileyfamily3 label="Baileyfamily3"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP3\]](#BP3){reference-type="eqref" reference="BP3"}. Then for $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily3eq}
        H_p^{(3)}(q) = q^{-1}\sum_{k=0}^{N-1} (-1)^k q^{\binom{k+1}{2} +(p-1)(k^2+k)} \alpha_k.$$
:::

::: theorem
[]{#Baileyfamily4 label="Baileyfamily4"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP4\]](#BP4){reference-type="eqref" reference="BP4"}. Then for $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily4eq}
        H_p^{(4)}(q)  = \sum_{k=0}^{N-1} (-1)^k q^{\binom{k+1}{2} + (p-1)(k^2+k)} \alpha_k.$$
:::

::: theorem
[]{#Baileyfamily5 label="Baileyfamily5"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP5\]](#BP5){reference-type="eqref" reference="BP5"}. Then for $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily5eq}
        H_p^{(8)}(q) = -q(1-q)\sum_{k=0}^{N-1} (-1)^k q^{\binom{k+1}{2} +(p-1)(k^2+k)} \alpha_k.$$
:::

::: theorem
[]{#Baileyfamily6 label="Baileyfamily6"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP6\]](#BP6){reference-type="eqref" reference="BP6"}. Then for $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily6eq}
        H_p^{(1)}(q)  = -q^{-1}(1-q)\sum_{k=0}^{N-1} (-1)^k q^{\binom{k+1}{2} +(p-1)(k^2+k)} \alpha_k.$$
:::

::: theorem
[]{#Baileyfamily7 label="Baileyfamily7"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP7\]](#BP7){reference-type="eqref" reference="BP7"}. For $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily7eq}
        H_p^{(4)}(q)  = q^{p-1}\sum_{k=0}^{N-1} (-1)^k q^{-\binom{k+1}{2}} (q^{p(k^2+2k)} \alpha_k)^*.$$
:::

::: theorem
[]{#Baileyfamily8 label="Baileyfamily8"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP8\]](#BP8){reference-type="eqref" reference="BP8"}. For $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily8eq}
        H_p^{(9)}(q) = q^{p}\sum_{k=0}^{N-1} (-1)^k q^{-\binom{k+1}{2}} (q^{p(k^2+2k)} \alpha_k)^*.$$
:::

For the last two results we define $$\label{alphatilde}
\widehat{\alpha}_k = \frac{(1-q)}{1-q^{k+1}}\alpha_k.$$

::: theorem
[]{#Baileyfamily9 label="Baileyfamily9"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP9\]](#BP9){reference-type="eqref" reference="BP9"}. For $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily9eq}
        \begin{aligned}
            -\frac{1}{2} + H_p^{(2)}(q)
            &= q^{p}\left(\sum_{k=0}^{N-2} (-1)^{k} q^{-\binom{k+1}{2} + p(k^2+2k)} \widehat{\alpha}_k + \frac{1}{2} q^{-p}\widehat{\alpha}_{N-1}\right).
        \end{aligned}$$
:::

::: theorem
[]{#Baileyfamily10 label="Baileyfamily10"} Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP10\]](#BP10){reference-type="eqref" reference="BP10"}. For $p \geq 1$ and $q$ any primitive $N$th root of unity we have $$\label{Baileyfamily10eq}
        \begin{aligned}
            -\frac{1}{2} + H_p^{(10)}(q)
            &= q^{p}\left(\sum_{k=0}^{N-2} (-1)^{k} q^{-\binom{k+1}{2} + p(k^2+2k)} \widehat{\alpha}_k + \frac{1}{2} q^{-p}\widehat{\alpha}_{N-1}\right).
        \end{aligned}$$
:::

::: proof
*Proof of Theorem [\[Baileyfamily1\]](#Baileyfamily1){reference-type="ref" reference="Baileyfamily1"}.* Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP1\]](#BP1){reference-type="eqref" reference="BP1"}. Using [\[qPochn-k\]](#qPochn-k){reference-type="eqref" reference="qPochn-k"} we compute that $$\label{betan-1-p1}
\beta_{N-1-n_p} = \frac{(q^{1-2N})_{2n_p} q^{4Nn_p-2n_p^2-n_p}}{(q^2)_{2N-2}}.$$ Inserting this into [\[keychainlemmaeq\]](#keychainlemmaeq){reference-type="eqref" reference="keychainlemmaeq"} we obtain $$\begin{aligned}
\sum_{N-1 \geq n_p \geq \cdots \geq n_1\geq 0}& \frac{q^{(N-n_p-1)(N-n_p)}(q^{1-2N})_{2n_p} q^{4Nn_p-2n_p^2-n_p}}{(q)_{n_p}} \prod_{i=1}^{p-1} q^{(N-n_i-1)(N-n_i)} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \\
&= \frac{(q^2)_{2N-2}}{(q)_{N-1}(q^2)_{N-1}} \sum_{k=0}^{N-1} \frac{(q^{1-N})_k}{(q^{1+N})_k}(-1)^k q^{Nk -\binom{k+1}{2} + p(k^2+k)} \alpha_k.
\end{aligned}$$ Now we let $q$ be a primitive $N$th root of unity. The terms $\frac{(q^2)_{2N-2}}{(q)_{N-1}(q^2)_{N-1}}$ and $\frac{(q^{1-N})_k}{(q^{1+N})_k}$ become $1$, as do all other instances of $q^N$. The result is [\[Baileyfamily1eq\]](#Baileyfamily1eq){reference-type="eqref" reference="Baileyfamily1eq"}. ◻
:::

::: proof
*Proofs of Theorems [\[Baileyfamily2\]](#Baileyfamily2){reference-type="ref" reference="Baileyfamily2"}--[\[Baileyfamily6\]](#Baileyfamily6){reference-type="ref" reference="Baileyfamily6"}.* The proofs of Theorems [\[Baileyfamily2\]](#Baileyfamily2){reference-type="ref" reference="Baileyfamily2"}--[\[Baileyfamily6\]](#Baileyfamily6){reference-type="ref" reference="Baileyfamily6"} closely resemble the proof of Theorem [\[Baileyfamily1\]](#Baileyfamily1){reference-type="ref" reference="Baileyfamily1"}. The only difference is the initial Bailey pair $(\alpha_k,\beta_k)$. Therefore we limit ourselves to noting the expression for $\beta_{N-1-n_p}$ in each case. For the Bailey pairs in [\[BP2\]](#BP2){reference-type="eqref" reference="BP2"}--[\[BP6\]](#BP6){reference-type="eqref" reference="BP6"}, we have, respectively, $$\beta_{N-1-n_p} = \frac{(q^{1-2N})_{2n_p} q^{4Nn_p-2n_p^2-2n_p + N-1}}{(q^2)_{2N-2}},$$ $$\label{betan-1-p3}
\beta_{N-1-n_p} = \frac{(q^{1-2N})_{2n_p} q^{4Nn_p-2n_p^2-n_p + (N-n_p-1)^2}}{(q^2)_{2N-2}},$$ $$\beta_{N-1-n_p} = \frac{(q^{1-2N})_{2n_p} q^{4Nn_p-2n_p^2-n_p + (N-n_p-1)^2 + (N-n_p-1)}}{(q^2)_{2N-2}},$$ $$\beta_{N-1-n_p} = \frac{(q^{2-2N})_{2n_p} q^{4Nn_p-2n_p^2-3n_p}}{(q)_{2N-2}}$$ and $$\beta_{N-1-n_p} = \frac{(q^{2-2N})_{2n_p} q^{4Nn_p-2n_p^2-3n_p + (N-1-n_p)^2 - (N-1-n_p)}}{(q)_{2N-2}}.$$ Using these in [\[keychainlemma\]](#keychainlemma){reference-type="eqref" reference="keychainlemma"} and calculating as in the proof of Theorem [\[Baileyfamily1\]](#Baileyfamily1){reference-type="ref" reference="Baileyfamily1"} we obtain [\[Baileyfamily2eq\]](#Baileyfamily2eq){reference-type="eqref" reference="Baileyfamily2eq"}--[\[Baileyfamily6eq\]](#Baileyfamily6eq){reference-type="eqref" reference="Baileyfamily6eq"}. ◻
:::

The proofs of Theorems [\[Baileyfamily7\]](#Baileyfamily7){reference-type="ref" reference="Baileyfamily7"} and [\[Baileyfamily8\]](#Baileyfamily8){reference-type="ref" reference="Baileyfamily8"} are similar, the only difference being the use of Proposition [\[keychainlemmabis\]](#keychainlemmabis){reference-type="ref" reference="keychainlemmabis"} instead of Proposition [\[keychainlemma\]](#keychainlemma){reference-type="ref" reference="keychainlemma"}.

::: proof
*Proofs of Theorems [\[Baileyfamily7\]](#Baileyfamily7){reference-type="ref" reference="Baileyfamily7"}--[\[Baileyfamily8\]](#Baileyfamily8){reference-type="ref" reference="Baileyfamily8"}.* Let $(\alpha_k,\beta_k)$ denote the Bailey pair in [\[BP7\]](#BP7){reference-type="eqref" reference="BP7"}. Note that the $\beta_k$ is the same as in [\[BP3\]](#BP3){reference-type="eqref" reference="BP3"}, and so $\beta_{N-1-n_p}$ is given by [\[betan-1-p3\]](#betan-1-p3){reference-type="eqref" reference="betan-1-p3"}. Using this in [\[keychainlemmabiseq\]](#keychainlemmabiseq){reference-type="eqref" reference="keychainlemmabiseq"} we have $$\begin{aligned}
\sum_{N-1 \geq n_p \geq \cdots \geq n_1\geq 0}& \frac{q^{(N-n_p)^2-1} (q^{1-2N})_{2n_p} q^{4Nn_p-2n_p^2-n_p + (N-n_p-1)^2}}{(q)_{n_p}} \prod_{i=1}^{p-1} q^{(N-n_i-1)(N-n_i+1)} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \\
&= \frac{(q^2)_{2N-2}}{(q)_{N-1}(q^2)_{N-1}} \sum_{k=0}^{N-1} \frac{(q^{1-N})_k}{(q^{1+N})_k}(-1)^k q^{Nk -\binom{k+1}{2}} (q^{p(k^2+2k)} \alpha_k)^*.
\end{aligned}$$ Letting $q$ be a primitive $N$th root of unity gives [\[Baileyfamily7eq\]](#Baileyfamily7eq){reference-type="eqref" reference="Baileyfamily7eq"}. Theorem [\[Baileyfamily8\]](#Baileyfamily8){reference-type="ref" reference="Baileyfamily8"} follows in the same way using the Bailey pair in [\[BP8\]](#BP8){reference-type="eqref" reference="BP8"}. ◻
:::

::: proof
*Proofs of Theorems [\[Baileyfamily9\]](#Baileyfamily9){reference-type="ref" reference="Baileyfamily9"}--[\[Baileyfamily10\]](#Baileyfamily10){reference-type="ref" reference="Baileyfamily10"}.* For Theorem [\[Baileyfamily9\]](#Baileyfamily9){reference-type="ref" reference="Baileyfamily9"} we use [\[BP9\]](#BP9){reference-type="eqref" reference="BP9"} in Proposition [\[keychainlemmater\]](#keychainlemmater){reference-type="ref" reference="keychainlemmater"} to obtain $$\label{obtained9}
\begin{aligned}
\sum_{N-1 \geq n_p \geq \cdots \geq n_1\geq 0}& \frac{q^{(N-n_p-1)(N-n_p+1)} q^{2Nn_p - n_p^2 + N^2-N}(q^{1-2N})_{2n_p}}{(1+q^{N-n_p})(q)_{n_p}} \prod_{i=1}^{p-1} q^{(N-n_i-1)(N-n_i+1)} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \\
&= \frac{(q)_{2N-1}}{(q)_{N-1}(q)_{N}} \sum_{k=0}^{N-1} \frac{(q^{1-N})_k}{(q^{2+N})_k}(-1)^k q^{Nk -\binom{k+1}{2} + p(k^2+2k)} \alpha_k.
\end{aligned}$$ Letting $q$ be a primitive $N$th root of unity the left-hand side of ([\[obtained9\]](#obtained9){reference-type="ref" reference="obtained9"}) becomes $$\label{next}
q^{-p}\sum_{n_p \geq \cdots \geq n_1 \geq 0} \frac{q^{n_p}(q^{n_p+1})_{n_p}}{(1+q^{n_p})} \prod_{i=1}^{p-1} q^{n_i^2} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix}.$$ Note that $$\frac{(q^{n_p+1})_{n_p}}{(1+q^{n_p})} = 
\begin{dcases}
(q^{n_p})_{n_p} & \text{if $n_p > 0$} \\
\frac{1}{2} & \text{if $n_p = 0$}
\end{dcases}$$ and so ([\[next\]](#next){reference-type="ref" reference="next"}) when $q$ is a primitive $N$th root of unity is $$q^{-p}\left(-\frac{1}{2} + \sum_{n_p \geq \cdots \geq n_1 \geq 0} q^{n_p}(q^{n_p})_{n_p} \prod_{i=1}^{p-1} q^{n_i^2} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \right).$$

Now letting $q$ be a primitive $N$th root of unity on the right-hand side of [\[obtained9\]](#obtained9){reference-type="eqref" reference="obtained9"}, the prefactor becomes $1$ as usual. As for the term $\frac{(q^{1-N})_k}{(q^{2+N})_k}$, it does not become $1$ as before. But when multiplied by $(1-q^{k+1})/(1-q)$, it becomes $1$ for $k < N-1$ while for $k = N-1$ it is $\frac{(1-q^N)}{(1-q^{2N})} \to \frac{1}{2}$. This observation accounts for the use of $\widehat{\alpha}_k$ and the splitting of the sum on the right-hand side of [\[Baileyfamily9eq\]](#Baileyfamily9eq){reference-type="eqref" reference="Baileyfamily9eq"}. Here, we also use that $q^{-\binom{N}{2} + pN^2} = (-1)^{N+1}$. This gives Theorem [\[Baileyfamily9\]](#Baileyfamily9){reference-type="ref" reference="Baileyfamily9"}. Theorem [\[Baileyfamily10\]](#Baileyfamily10){reference-type="ref" reference="Baileyfamily10"} follows in the same way using [\[BP10\]](#BP10){reference-type="eqref" reference="BP10"} in Proposition [\[keychainlemmater\]](#keychainlemmater){reference-type="ref" reference="keychainlemmater"}. ◻
:::
