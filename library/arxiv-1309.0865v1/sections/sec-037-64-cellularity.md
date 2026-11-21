---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-037-64-cellularity
section_title: "Cellularity"
section_number: 6.4
pages: 64-65
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.949
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
We assume Theorem \ref{homspacetheorem}, so that Hom spaces are free left $R$-modules and localization is injective on Hom spaces.

\begin{claim} For any $w \in W$, let $\XC_w$ be the set of maps in $\DC$ which, after localization, induce the zero map on every $Q_w$ summand of their source object. Then $\XC_w$ is a
2-sided ideal in $\DC$. \end{claim}

\begin{proof} Left to the reader. \end{proof}

\begin{claim} The light leaves map $\LLL_{w,\eb,\fb}$ will be in $\XC_v$ for any $v \nleq w$. \end{claim}

\begin{proof} This follows from Bruhat upper-triangularity. \end{proof}

For any $I \subset W$, let $\LLL_I$ denote the span of all $\LLL$ maps which factor through $w \in I$. Now let $I \subset W$ be an ideal with respect to the Bruhat order. In other words,
if $w \in I$ and $v \le w$ then $v \in I$.

\begin{claim} When $I$ is an ideal, $\LLL_I$ is a 2-sided ideal in $\DC$. It is equal to $\XC_{W \setminus I}$, the intersection of the ideals $\XC_w$ for each $w \notin I$. \end{claim}

\begin{proof} We need only show that $\LLL_I$ is equal to $\XC_{W \setminus I}$, for the latter is clearly a 2-sided ideal. The inclusion $\LLL_I \subset \XC_{W \setminus I}$ follows from
the previous claim.

Now suppose that $\phi \in \Hom({\un{w}},{\un{y}})$ is in $\XC_{W \setminus I}$, and write $\phi$ as a linear combination of $\LLL$ maps. Unless $\phi$ is zero, some $\LLL_{w,\fb,\eb}$ has a
non-zero coefficient. Choose $w$, $\eb$, and $\fb$ successively such that each is maximal in the Bruhat/path dominance order relative to the constraint that, with the previous choices,
there is a nonzero coefficient for $\LLL_{w,\fb,\eb}$ in $\phi$. Because of upper triangularity, this is the only coefficient which can possibly contribute to a map from $Q_\eb$ to
$Q_{\fb}$, and it does contribute in a non-zero way. Therefore $\phi$ induces a nonzero map on $Q_\eb$, implying that $w \in I$. Since this is true for each maximal choice of $w$, we see
that $\phi \in \LLL_I$. \end{proof}

It is clear that if ${\un{w}}$ and $\un{w}'$ are rexes for $w \in W$, then any two rex moves $B_{\un{w}} \to B_{\un{w}'}$ are equal modulo $\LLL_{< w}$. Both rex moves are in $\LLL_{\le w}$, and induce the identity map on the unique $Q_w$ summand after localization.

Now let ${\un{y}}={\un{x}}$. Recall that $\LLL_{w,\fb,\eb} = \oLL_{{\un{x}},\fb} \circ \LL_{{\un{x}},\eb}$, factoring through ${\un{w}}$ in the middle. Suppose we compose them in the opposite order, to get an
endomorphism of $B_{\un{w}}$. We have an $\LLL$ basis for endomorphisms of $B_{\un{w}}$ as well, and there is a \emph{unique} light leaves morphism which induces a nonzero map on
the unique standard summand $Q_w$. This map can be any rex move, and though we often assume for convenience that it is the identity, this assumption is not necessary. Let $\psi(\eb,\fb)$
denote the coefficient of this light leaves morphism inside the composition $\LL_{{\un{w}},\eb} \circ \oLL_{{\un{w}},\fb}$.

\begin{claim} Let ${\un{x}},{\un{y}},{\un{z}}$ be arbitrary. Fix $w \in W$, and choose subsequences $\eb$ of ${\un{x}}$, $\fb$ and $\gb$ of ${\un{y}}$, and $\hb$ of ${\un{z}}$ which all express $w$. Then the
composition $\LLL_{\hb,\gb} \LLL_{\fb,\eb} \co B_{\un{x}} \to B_{\un{z}}$ is equal to $\psi(\gb,\fb) \LLL_{\hb,\eb}$ modulo $\LLL_{< w}$. \end{claim}

\begin{proof} $\LLL_{\hb,\gb} \LLL_{\fb,\eb}$ is a composition of four maps, the inner ones being $\LL_{{\un{y}},\gb} \oLL_{{\un{y}},\fb}$. This composition is equal to $\psi(\gb,\fb)$ times the
identity of $B_{{\un{w}}}$, plus maps in $\LLL_{< w}$. Therefore the overall composition is equal to $\psi(\gb,\fb) \oLL_{{\un{z}},\hb} \LL_{{\un{w}},\eb}$ modulo $\LLL_{< w}$, as desired. \end{proof}

\begin{claim} Let $a \co B_{\un{y}} \to B_{\un{z}}$ be an arbitrary morphism, and $\LLL_{w,\eb,\fb}$ be a light leaves map $B_{\un{x}} \to B_{\un{y}}$ factoring through the rex $B_{\un{w}}$. Then $a \LLL_{w,\eb,\fb}
= \sum_{\fb'} r_a(\fb,\fb') \LLL_{w,\eb,\fb'}$ modulo $\LLL_{< w}$. The sum runs over subexpressions $\fb'$ of ${\un{z}}$ expressing $w$. The coefficients $r_a(\fb,\fb')$ do not depend on $\eb$. \end{claim}

\begin{proof} Write $a \LLL_{\eb,\fb} = a \oLL_{{\un{y}},\fb} \LL_{{\un{w}},\eb}$, and consider $a \oLL_{{\un{y}},\fb}$ as a map from $B_{\un{w}} \to B_{\un{z}}$. The space of maps $B_{\un{w}} \to B_{\un{z}}$ modulo
$\LLL_{< w}$ is spanned by $\{ \oLL_{{\un{z}},\fb'}\}$ over all $\fb'$, so that $a \oLL_{{\un{y}},\fb} = \sum_{\fb'} r_a(\fb,\fb') \oLL_{{\un{z}},\fb'}$ modulo lower terms. Composing with $\LL_{{\un{x}},\eb}$
once more, we get the desired result. \end{proof}

\begin{defn} Let $\iota \co \DC \to \DC^{\op}$ denote the antiinvolution which preserves objects and flips diagrams upside-down. \end{defn}

Note that this reverses vertical composition, but not horizontal composition ($\iota$ is monoidal and contravariant). Clearly $\iota(\LLL_{\fb,\eb}) = \LLL_{\eb,\fb}$.

For the definition and basic properties of cellular categories, see \cite{West}.

\begin{prop} The category $\DC$ is cellular, with cellular basis $\LLL$ (for any appropriate choice of $\LLL$ maps) and antiinvolution $\iota$. \label{Discellular} \end{prop}

This proposition follows from the previous claim. The cells correspond to $w \in W$ with the Bruhat order, and the set $M({\un{x}},w)$ consists of all subsequences of ${\un{x}}$ expressing $w$. We do not know of any interesting interactions between the cellular structure and the monoidal structure.
