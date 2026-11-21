---
doc_id: 1172-2
doc_title: "L^2-torsion of 3-manifolds"
section_id: sec-008-34-写像類群のmagnus-表現
section_title: "写像類群のMagnus 表現"
section_number: 34
pages: 15-17
source_pdf: 1172-2.pdf
source_sha256: 390665341d5b7522
toc_source: inferred
doc_brief: "L^2-torsion of 3-manifolds — 14 sections: Front matter; 序章; お礼の言葉"
---
写像類群のMagnus 表現
ここまで述べてきたことを写像類群のMagnus 表現の観点から書き直して
みます。
$\mathcal{M}_{g,1}$ を
$\Sigma_{g,1}$ の写像類群とします。
$\mathcal{M}_{g,1}$ のMagnus 表現とは、$\mathcal{M}_{g,1}$
を
$\Gamma=\langle x_{1}, \ldots, x_{2}\rangle \mathit{9}$ の自己同型の部分群と見なして、Fox の自由微分を用
いて
$r: \mathcal{M}_{g,1}\ni\varphi-t(\frac{\partial\varphi_{*}(x_{j})}{\partial x_{i}})_{i,j}\in GL(2_{\mathit{9}};\mathbb{Z}\mathrm{r})$
と定義します。ここで、
$GL(2g;\mathbb{Z}\Gamma)\ni A\vdasharrow\overline{A}\in GL(2g;\mathbb{Z}\Gamma)$
は各成分毎に
$\mathbb{Z}\Gamma\ni\sum_{g}\lambda g\mathit{9}-t\sum_{g}\lambda g^{-1}\mathit{9}\in \mathbb{Z}\pi$
を考えることにより定まる写像です。
このMagnus 表現を使うと前のL\"uck の公式が言っていることは、
$\rho(W_{\varphi})$
は
$r(\varphi)$ の非可換なFuglede-Kadison 行列式を使った特性多項式ということ
です。ここで特性多項式と言っているのは、行列
$A\in GL(2g;\mathbb{Z}\mathrm{r})$ に対して、
行列$tI-A$ を
$M(2g;\mathbb{Z}\pi)$ の中の行列と考えてその行列式を取ると言う意味
です。もう少し詳しく説明しましょう。群
$\pi$ の表示を固定し、関係子
$r_{i}=t_{X_{i}}t-1(\varphi*(X_{i}))-1$
にFox の自由微分を作用させて、群環係数の行列
$A$ を定義しました。
ここ
で、$r_{i}=1$ を変型して$tx_{i}t^{-1}-\varphi_{*}(x_{i})=0$ とし、この左辺に自由微分を作用
15
させて、すべてをそれらで置き換えても
$\rho$ の値は変わらないことは容易に分
かります。そこで
$\rho(W_{\varphi})$ は、このようにして得られる行列$tI-r(\varphi)$ の行列
式と言うことができます。また、
$\det(tI-r(\varphi))=\det(tI-tr(\varphi))$
も容易に分かります。
では、
$\rho_{k}$ の場合はどうかと考えてみると、これは射影
$p_{k}$ :
$\Gammaarrow N_{k}$
から誘導される準同型をMagnus 表現と合成して得られる
$r_{k}$ :
$\mathcal{M}_{g,1}arrow GL(2g;\mathbb{Z}N_{k})$
のFuglede-Kadison 行列式による特性多項式と考えることができます。
16
