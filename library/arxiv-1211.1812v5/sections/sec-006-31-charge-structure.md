---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-006-31-charge-structure
section_title: "Charge structure."
section_number: 3.1
pages: 14-16
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.95
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
To introduce the charge structure we follow the standard way and, given $a \in \Delta$, define the set

${\bf loc}R_a \subseteq {\bf end}R_a$

whose elements are \*-endomorphims

$$\label{eq.C0}
\rho \in {\bf end}R_a  \ \ | \ \  \exists e < a 
\ \ {\mathrm{fulfilling}} \ \
\left\{
\begin{array}{ll}
\rho(R_o) \subseteq R_o \ , \ \forall o \supseteq e ,  o < a ,
\\
\rho = id_{R_o} \ , \ \forall o \perp e ,  o < a \ .
\end{array}
\right.$$

In the sequel we shall keep in evidence the *localization region* $e \in \Delta^a$ by writing $\rho_e \equiv \rho$. Note that

$\tau_e := \rho_e \circ \sigma_e \in {\bf loc}R_a$, $\forall \rho_e,\sigma_e \in {\bf loc}R_a$.

We now consider the category $Z^1_c(\EuFrak{R})_{< a}$ with objects pairs $(z,\rho) \equiv z_\rho$, where

$$z = \{ z(b) \in UR_{|b|} \}_{b \in \Sigma_1(\Delta^a)} 
\ \ , \ \
\rho = \{ \rho_e \in {\bf loc}R_a \}_{e \in \Delta^a}
\ ,$$

fulfill

$$\label{eq.C1}
\left\{
\begin{array}{ll}
dz(c)=1 \ \ , \ \ \forall c \in \Sigma_2(\Delta^a) \ ,
\\
z(b) \cdot \rho_{\partial_1b}(t) = \rho_{\partial_0b}(t) \cdot z(b)
\ \ , \ \
\forall b \in \Sigma_1(\Delta^a) \ , \ t \in R_a \ .
\end{array}
\right.$$

The first equation says that $z$ is a cocycle defined on the \"local\" poset $\Delta^a$. The second one yields an interpretation of $z$ as the flat connection transporting from ${\partial_1 b}$ to ${\partial_0 b}$ the quantum charge represented by $\rho$ (see [@Rob §25-28] or the friendly [@Dop11]) and implies that $z$ uniquely determines $\rho_e$ on $R_e$ for any $e < a$: for, if $o \in \Delta^a$ with $o \perp e$ and $p : e \to o$ is a path in $\Delta^a$ then

$$\label{eq.int0}
\rho_e(T') \ \stackrel{ (\ref{eq.C1}) }{=} \ z(p)^* \rho_o(T') z(p) \ , \ \forall T' \in R_a
\ \ \Rightarrow \ \
\rho_e(T) \ \stackrel{ (\ref{eq.C0}) }{=} \ z(p)^* T z(p) \ \ , \ \ \forall T \in R_e \ .$$

The arrows of $Z^1_c(\EuFrak{R})_{< a}$ are given by

$$\label{eq.int00}
(z_\rho,w_\sigma)
\ := \
\{ \ t = \{ t_e \in R_e \}_{e \in {\Delta^a}} 
     \ : \
     t_{\partial_0b} z(b)  =  w(b) t_{\partial_1b}
     \ , \
     \forall b \in \Sigma_1(\Delta^a) \ \}
\ .$$

Note that $\rho,\sigma$ play no role in the definition of $(z_\rho,w_\sigma)$. Applying repeatedly ([\[eq.C1\]](#eq.C1){reference-type="ref" reference="eq.C1"}) to a path

$p : e \to o$, $p = b_n * \ldots * b_1$, with $e \perp o < a$,

we have that if $t \in (z_\rho,w_\sigma)$ then

$$t_o z_\rho(p) \ = \ w_\sigma(p) t_e
\ \ \Rightarrow \ \
T w_\sigma(p) t_e = T t_o z_\rho(p) \stackrel{Einstein \ causality}{=} t_o T z_\rho(p)
\ \ , \ \
\forall T \in R_e
\ ,$$

so, applying ([\[eq.int0\]](#eq.int0){reference-type="ref" reference="eq.int0"}),

$$\label{eq.int}
\sigma_e(T) \, t_e \ = \ t_e \, \rho_e(T)
\ \ , \ \qquad
\forall t \in (z_\rho,w_\sigma)
\ , \
e < a
\ , \
T \in R_e
\ .$$

We define the tensor product on $Z^1_c(\EuFrak{R})_{< a}$. To this end, given

$z_\rho , w_\sigma$, $z'_{\rho'} , w'_{\sigma'} \in$ ${\bf obj} Z^1_c(\EuFrak{R})_{< a}$, $t \in (z_\rho,z'_{\rho'})$, $s \in (w_\sigma,w'_{\sigma'})$,

we set

$$\label{eq.tens.z1}
\left\{
\begin{array}{ll}
\{ z \otimes w \}_{\rho \circ \sigma}(b) := z_\rho(b) \rho_{\partial_1b}(w_\sigma(b))
\ \ , \ \
\forall  e < a
\ , \
b \in \Sigma_1(\Delta^a) \ ,

\\

(t \otimes s)_e := t_e \rho_e(s_e)
\ , \ 
\forall  e < a \ .

\\
\end{array}
\right.$$

The fact that the above-defined relations yield a tensor product on $Z^1_c(\EuFrak{R})_{< a}$ follows by elementary \*-algebraic computations (analogous to those in [@Rob §27], [@Ruz05 §4.2.1]), anyway for convenience of non-specialists we recall some of them.

A first point is that since any $\rho_e$, $e < a$, is a unital \*-endomorphism, we have that $z_\rho(b) \rho_{\partial_1b}(w_\sigma(b))$ is unitary. Moreover, ([\[eq.C0\]](#eq.C0){reference-type="ref" reference="eq.C0"}) implies that $z_\rho(b) \rho_{\partial_1b}(w_\sigma(b)) \in R_{|b|}$ for any $b \in \Sigma_1(\Delta^a)$. The cocycle relations follow by computing, for any $c \in \Sigma_2(\Delta^a)$,

$$\begin{array}{ll}
z_\rho(\partial_0c) \rho_{\partial_{10}c}(w_\sigma(\partial_0c)) \cdot
z_\rho(\partial_2c) \rho_{\partial_{12}c}(w_\sigma(\partial_2c)) & =

z_\rho(\partial_0c) z_\rho(\partial_2c) 
\rho_{\partial_{12}c}(w_\sigma(\partial_0c)) \rho_{\partial_{12}c}(w_\sigma(\partial_2c)) = \\ & =

z_\rho(\partial_1c) \rho_{\partial_{12}c}(w_\sigma(\partial_1c)) = \\ & =

z_\rho(\partial_1c) \rho_{\partial_{11}c}(w_\sigma(\partial_1c)) 
\ ,
\end{array}$$

having used repeatedly ([\[eq.C1\]](#eq.C1){reference-type="ref" reference="eq.C1"}), the composition rule of face maps $\partial_{12} = \partial_{11}$ (see ([\[eq.dd\]](#eq.dd){reference-type="ref" reference="eq.dd"}) or [@RR06 Eq.1]), and the cocycle relations of $z,w$.

Passing to the \"charges\", for any $t \in R_a$ we have

$$\begin{array}{ll}
z_\rho(b) \rho_{\partial_1b}(w_\sigma(b)) \cdot \{ \rho_{\partial_1b} \circ \sigma_{\partial_1b} \}(t)
& = \
z_\rho(b) \cdot \rho_{\partial_1b} ( w_\sigma(b) \sigma_{\partial_1b}(t) )
\ = \
\rho_{\partial_0b} ( \sigma_{\partial_0b}(t) w_\sigma(b) ) \cdot z_\rho(b)
\ = \\ & =
\{ \rho_{\partial_0b} \circ \sigma_{\partial_0b} \}(t) \cdot z_\rho(b) \rho_{\partial_1b}(w_\sigma(b)) \ ,
\end{array}$$

so ([\[eq.C1\]](#eq.C1){reference-type="ref" reference="eq.C1"}(2)) is fulfilled for $z \otimes w$ and

$(z \otimes w)_{\rho \circ \sigma} \in {\bf obj \ }Z^1_c(\EuFrak{R})_{<a}$.

To verify that $t \otimes s$ is an arrow in

$( \ (z \otimes w)_{\rho \circ \sigma} \ , \ ( z' \otimes w')_{\rho' \circ \sigma'} \ )$

we compute

$$\begin{array}{lcl}
t_{\partial_0 b}\rho_{\partial_0 b}(s_{\partial_0 b}) \cdot z_\rho(b) \rho_{{\partial_1 b}}(w_\sigma(b)) & = &
t_{\partial_0 b}z_\rho(b) \cdot \rho_{\partial_1 b}(s_{\partial_0 b}w_\sigma(b)) = \\ & = &

z'_{\rho'}(b) t_{\partial_1 b}\rho_{\partial_1 b}(w'_{\sigma'}(b)) \rho_{\partial_1 b}(s_{\partial_1 b}) = \\ & \stackrel{ (\ref{eq.int}) }{=} &

z'_{\rho'}(b) \rho'_{\partial_1 b}(w'_{\sigma'}(b)) \cdot t_{\partial_1 b}\rho_{{\partial_1 b}}(s_{\partial_1 b})
\ ,
\end{array}$$

obtaining the desired relations.

::: rem
Let $\iota^a \in {\bf obj \ }Z^1_c(\EuFrak{R})_{< a}$ be the pair defined by the identity cocycle of $Z^1(\EuFrak{R})_{< a}$ and the constant family with element the identity $id_{R_a} \in {\bf aut}R_a$. Clearly $\iota^a$ is the identity object of the tensor product of $Z^1(\EuFrak{R})_{< a}$, and, given $x \in a$, we have

$${\mathbb C}1                      \ \subseteq \
(\iota^a,\iota^a)          \ = \ 
\cap_{e < a} R_e           \ \subseteq \ 
\cap_{e < a : x \in e} R_e \ \stackrel{(*)}{=} \ 
\cap_{a \ni x} R_a         \ \stackrel{(\ref{eq.Ap1})}{=} \ 
{\mathbb C}1 \ ,$$

where for the equality (\*) we used the fact that $\{ a \in \Delta : x \in a \}$ is downward directed. So $(\iota^a,\iota^a) = {\mathbb C}1$ and $Z^1_c(\EuFrak{R})_{< a}$ has a simple unit.
:::
