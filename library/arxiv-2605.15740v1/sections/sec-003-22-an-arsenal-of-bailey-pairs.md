---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-003-22-an-arsenal-of-bailey-pairs
section_title: "An arsenal of Bailey pairs"
section_number: 2.2
pages: 8-10
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.797
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
[]{#arseBP label="arseBP"} Here we collect all of the Bailey pairs we will use in the proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. There are eight Bailey pairs that we cite from the literature -- six Bailey pairs relative to $q$ and two Bailey pairs relative to $q^2$. First, we have four Bailey pairs relative to $q$ from Slater's list [@Sl p.463, A(2), A(4), A(6), A(8)]:

$$\label{BP1}
    \alpha_k = 
    \begin{cases}
        q^{6r^2 -r} & \text{if $k=3r-1$}, \\
        q^{6r^2 +r} & \text{if $k=3r$}, \\
        -q^{6r^2+5r+1} - q^{6r^2+7r+2} &\text{if $k=3r+1$}
    \end{cases}
    \ \ \ \ \text{and} \ \ \ \ \beta_k = \frac{1}{(q^2)_{2k}},$$

$$\label{BP2}
    \alpha_k = 
    \begin{cases}
        q^{6r^2 -4r} & \text{if $k=3r-1$}, \\
        q^{6r^2 +4r} & \text{if $k=3r$}, \\
        -q^{6r^2+8r+2} - q^{6r^2+4r} &\text{if $k=3r+1$}
    \end{cases}
\ \ \ \ \text{and} \ \ \ \ \beta_k = \frac{q^k}{(q^2)_{2k}},$$

$$\label{BP3}
    \alpha_k = 
    \begin{cases}
        q^{3r^2+r} & \text{if $k=3r-1$}, \\
        q^{3r^2-r} & \text{if $k=3r$}, \\
        -q^{3r^2+r} - q^{3r^2+5r+2} &\text{if $k=3r+1$}
    \end{cases}
\ \ \ \ \text{and} \ \ \ \ \beta_k = \frac{q^{k^2}}{(q^2)_{2k}}$$ and $$\label{BP4}
    \alpha_k = 
    \begin{cases}
        q^{3r^2 -2r} & \text{if $k=3r-1$}, \\
        q^{3r^2 +2r} & \text{if $k=3r$}, \\
        -q^{3r^2+4r+1} - q^{3r^2+2r} &\text{if $k=3r+1$}
    \end{cases}
\ \ \ \ \text{and} \ \ \ \ \beta_k = \frac{q^{k^2+k}}{(q^2)_{2k}}.$$

Next we have two Bailey pairs relative to $q$ from work of Warnaar [@Wa]:

$$\label{BP5}
    \alpha_k = (-1)^{\lfloor \frac{4k+1}{3} \rfloor}q^{\frac{k(2k-1)}{3}}\frac{(1-q^{2k+1})}{(1-q)}\chi(k \not \equiv 1 \pmod{3})
\ \ \ \ \text{and} \ \ \ \  \beta_k = \frac{1}{(q)_{2k}}$$ and $$\label{BP6}
    \alpha_k = (-1)^{\lfloor \frac{4k+1}{3} \rfloor}q^{\frac{k(k-2)}{3}}\frac{(1-q^{2k+1})}{(1-q)}\chi(k \not \equiv 1 \pmod{3}) \ \ \ \ \text{and} \ \ \ \ 
    \beta_k = \frac{q^{k^2-k}}{(q)_{2k}}.$$

Finally, we have two Bailey pairs relative to $q^2$. These are [@Si-Mc-Zi Eq. (2.34), $e \to 0$ and $e \to \infty$]: $$\label{BP7}
    \alpha_k = 
    \begin{dcases}
            0 &\text{if $k=3r-1$}, \\   
        \frac{(1-q^{6r+2})}{1-q^2}q^{3r^2-r} & \text{if $k=3r$}, \\
        -\frac{(1-q^{6r+4})}{1-q^2}q^{3r^2+r} & \text{if $k=3r+1$} 
    \end{dcases}
\ \ \ \ \text{and} \ \ \ \ 
    \beta_k = \frac{q^{k^2}}{(q^2)_{2k}}$$ and $$\label{BP8} 
    \alpha_k = 
    \begin{dcases}
             0 &\text{if $k=3r-1$}, \\
        \frac{(1-q^{6r+2})}{1-q^2}q^{6r^2+r} & \text{if $k=3r$}, \\
        -\frac{(1-q^{6r+4})}{1-q^2}q^{6r^2+5r+1} & \text{if $k=3r+1$}
    \end{dcases}
\ \ \ \ \text{and} \ \ \ \
    \beta_k = \frac{1}{(q^2)_{2k}}.$$

To these we add two Bailey pairs relative to $q^2$ which we were not able to locate in the literature.

::: lemma
The following two sequences are Bailey pairs relative to $q^2$: $$\label{BP9}
        \alpha_k = 
        \begin{dcases}
            \frac{(1-q^{k+1})}{1-q}\left(q^{3r^2-2r} - q^{3r^2-r}\right) & \text{if $k=3r-1$}, \\
            \frac{(1-q^{k+1})}{1-q}q^{3r^2+r} & \text{if $k=3r$}, \\
            -\frac{(1-q^{k+1})}{1-q}q^{3r^2+2r} &\text{if $k=3r+1$}
        \end{dcases}
        \ \ \ \ \text{and} \ \ \ \ \beta_k = \frac{q^{k^2+k}(1+q)}{(q^2)_{2k}(1+q^{k+1})}$$ and $$\label{BP10}
        \alpha_k = 
        \begin{dcases}
            \frac{(1-q^{k+1})}{1-q}\left(q^{6r^2-r} - q^{6r^2-2r}\right) & \text{if $k=3r-1$}, \\
            \frac{(1-q^{k+1})}{1-q}q^{6r^2+2r} & \text{if $k=3r$}, \\
            -\frac{(1-q^{k+1})}{1-q}q^{6r^2+7r+2} &\text{if $k=3r+1$}
        \end{dcases}
        \ \ \ \ \text{and} \ \ \ \ \beta_k = \frac{(1+q)}{(q^2)_{2k}(1+q^{k+1})}.$$
:::

::: proof
*Proof.* We require [@Lo.5 Eq. (2.4)], which says that if $(\alpha_k,\beta_k)$ is a Bailey pair relative to $a$, then $(\alpha_k^{\dag},\beta_k^{\dag})$ is a Bailey pair relative to $aq$, where $$\label{alphadag}
        \alpha_k^{\dag} = \frac{(1-aq^{2k+1})(aq/b)_k(-b)^kq^{\binom{k}{2}}}{(1-aq)(bq)_k} \sum_{j=0}^k \frac{(b)_j}{(aq/b)_j} (-b)^{-j} q^{-\binom{j}{2}} \alpha_j$$ and $$\label{betadag}
        \beta_k^{\dag} = \frac{(b)_k}{(bq)_k}\beta_k.$$ We apply this with $b = -q$ to the Bailey pair relative to $q$ in [\[BP4\]](#BP4){reference-type="eqref" reference="BP4"}. The resulting $\beta_k^{\dag}$ is clearly the $\beta_k$ in [\[BP9\]](#BP9){reference-type="eqref" reference="BP9"}, while $$\alpha_k^{\dag} = \frac{(1-q^{k+1})}{1-q} q^{\binom{k+1}{2}} \sum_{j=0}^k q^{-\binom{j+1}{2}}\alpha_j.$$ An induction argument on $k$ confirms that $\alpha_k^{\dag}$ equals $\alpha_k$ from [\[BP9\]](#BP9){reference-type="eqref" reference="BP9"}.

Next we recall that if $(\alpha_k,\beta_k)$ is a Bailey pair relative to $q^2$, then its dual [@An1] $(\alpha_k^d,\beta_k^d)$ is also a Bailey pair relative to $q^2$, where $$\alpha_k^d = q^{k^2+2k}\alpha_k(q^{-1}) \ \ \ \text{and} \ \ \ \beta_k^d = q^{-k^2-3k}\beta_k(q^{-1}).$$ Using the fact that $$(q^{-2};q^{-1})_{2k} = q^{-2k^2-3k}(q^2)_{2k},$$ a short calculation shows that [\[BP10\]](#BP10){reference-type="eqref" reference="BP10"} is the dual of [\[BP9\]](#BP9){reference-type="eqref" reference="BP9"}. ◻
:::
