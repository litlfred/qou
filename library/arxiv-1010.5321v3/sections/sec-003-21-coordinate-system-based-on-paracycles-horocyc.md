---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗"
section_id: sec-003-21-coordinate-system-based-on-paracycles-horocyc
section_title: "Coordinate system based on paracycles (horocycles)"
section_number: 2.1
pages: 2-3
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.982
doc_brief: "Formulas on hyperbolic volume ∗ — This paper collects some important formulas on hyperbolic volume."
---
![coordinate system based on paracycles.](vol1.eps)

Consider a parasphere of dimension $n-1$ and its pencil of rays of parallel lines. The last coordinate axis let be one of these rays, the origin will be the intersection of this line by the parasphere. The further axes are pairwise orthogonal paracycles. The coordinates of $P$ are $\left( \xi _1 ,\xi _2,\cdots ,\xi _n \right)^T,$ where the last coordinate is the distance of $P$ and the parasphere, while the further coordinates are the coordinates of the orthogonal projection $T$ with respect to the Cartesian coordinate system giving by the mentioned paracycles.

In $\mathbb{R}^n$ we can correspond to $P$ a point $p$ (see on Fig.1) with ordinary Cartesian coordinates: $$\left( x_1,x_2,\cdots,x_n \right)^T=
\left( e^{-\frac{\xi_n}{k}}\xi_1, e^{-\frac{\xi_n}{k}}\xi_2,\cdots ,e^{-\frac{\xi_n}{k}}\xi_{n-1},\xi _n\right)^T.$$ By definition let the volume of a Jordan measurable set $D$ be $$v(D):=v_n\int \limits_{D^\star}  \mathrm{d}x_1\cdots \mathrm{d}x_n,$$ where $D^\star$ is the image of $D$ by the above mapping and $v_n$ is a constant which we will choose later. Our first formula on the volume is: $$v(D)=v_n\int\limits_{D} e^{-(n-1)\frac{\xi_n}{k}} \mathrm{d}\xi_1\cdots \mathrm{d}\xi_n,$$ depending on the coordinates of the points of $D$, with the given system of coordinates. Let now the domain $D=[0,a_1]\times \cdots\times [0,a_{n-1}]$ be a sector of parallel segments of length $a_n$ based on a coordinate-brick of the corresponding parasphere, then $$v(D)=v_n\int\limits_{0}^{a_1} \cdots \int\limits_{0}^{a_n} e^{-(n-1)\frac{\xi_n}{k}} \mathrm{d}\xi_n \cdots\mathrm{d}\xi_1=\frac{kv_n}{n-1}\prod \limits_{i=1}^{n-1} a_i\left[-e^{-(n-1)\frac{a_n}{k}}+e^0\right]=$$ $$=\frac{kv_n}{n-1}
\prod \limits_{i=1}^{n-1} a_i[1-e^{-(n-1)\frac{a_n}{k}}].$$ If $a_n$ tends to infinity and $a_i=1$ for $i=1\cdots (n-1)$, then the volume is equal to $\frac{kv_n}{n-1}$. Note that J.Bolyai and N.I.Lobachevski used the value $v_n=1$ so in their calculations the value of the volume is independent from the dimension but depends on the constant $k$ which determine the measure of the curvature of the space. We follows them we will determine the constant $v_n$ such that for every fixed $k$ the value of the measure of a thin layer divided by its height tends to the value of the measure of the limit figure of lower dimension. Now the limit: $$\lim\limits_{a_n\rightarrow \infty}\frac{v(D)}{a_n}=\frac{kv_n}{n-1}
\prod \limits_{i=1}^{n-1} a_i\lim\limits_{a_n\rightarrow \infty}\frac{[1-e^{-(n-1)\frac{a_n}{k}}]}{a_n}=v_n\prod \limits_{i=1}^{n-1} a_i,$$ is equal to $v_{n-1}\prod \limits_{i=1}^{n-1} a_i$ showing that $1=v_1=v_2=\ldots =v_n=\ldots$.

Thus $v_n=1$ as it used by earlier. On the other hand if for a fixed $n$ the number $k$ tends to infinity the volume of a body tends to the euclidean volume of the corresponding euclidean body. In every dimension $n$ we also have a $k$ for which the corresponding hyperbolic $n$-space contains a natural body with unit volume, if $k$ is equal to $n-1$ then the volume of the paraspheric sector based on a unit cube of volume $1$ is also $1$.

So with respect to paracycle coordinate system our volume function by definition is $$v(D)=\int\limits_{D} e^{-(n-1)\frac{\xi_n}{k}} \mathrm{d}\xi_1\cdots \mathrm{d}\xi_n.$$
