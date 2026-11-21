---
doc_id: 1172-2
doc_title: "L^2-torsion of 3-manifolds"
section_id: sec-004-23-l2-torsion-の計算例
section_title: "$L^{2}$-torsion の計算例"
section_number: 2.3
pages: 8-11
source_pdf: 1172-2.pdf
source_sha256: 390665341d5b7522
toc_source: inferred
doc_brief: "L^2-torsion of 3-manifolds — 14 sections: Front matter; 序章; お礼の言葉"
---
$L^{2}$-torsion の計算例
前節でのL\"uck の定理を用いて、基本群の表示から
$L^{2}$-torsion の
$\mathrm{l}\mathrm{o}\mathrm{g}\mathrm{a}\mathrm{r}\mathrm{i}\mathrm{t}\mathrm{h}\mathrm{m}\text{、}$
したがって本質的にそのsimplicial volume を求めてみます。
例21
まず、8 の字結び目
$4_{1}$ を考えることにします。よく知られているよ
うに、
$S^{3}$ におけるその補空間には双曲的3 次元多様体の構造が入ります。し
たがって、この場合の
$L^{2}$ -torsion の計算は、双学的体積を与えることになり
ます。
さて、$\pi=\pi_{1}(4_{1})$ の表示として、
$S^{1}$ 上の1 点穴あきト一ラス束として得
られるものを採用します:
$\pi=\langle x,y,t|txt^{-1}y^{-}1=tyt^{-1}xy-3=1\rangle$ .
このとき、Fox 行列は
で与えられます。ここで、
$S^{1}$ 方向の生成元
$t$ に関する列を除いて得られる正
方行列をL\"uck の定理における行列
$A$ とします(原論文とは、抜いている列
が異なることに注意)
:
$A=$
.
このとき、$K\geq||R_{A}||_{\infty}$ として$K=4$ がとれるので、$B=16-AA^{*}$ とお
けば、$B=$
,
$\lambda(y, t)=11+t+t^{-1}-2y-2y-1-y^{2}-y^{-2}+ty^{-1}+ty^{-2}+yt^{-1}+y^{2}t^{-1}$
となり、
$L^{2}$-torsion は次で与えられます:
8
$\log\rho(4_{1})=-2\cdot 2\log K+\sum p=\infty 1\frac{1}{p}\mathrm{t}\mathrm{r}\mathbb{C}\pi((1-K^{-}2AA*))$
$=-8 \log 2+\sum_{p=}\infty 1\frac{1}{p\cdot 16^{p}}\mathrm{t}\mathrm{r}_{\mathbb{C}}\pi(B^{p})$ .
この公式を用いた計算機による数値実験の結果は以下の表1 のとおりです。
ここで、表中の
$\log\rho(4_{1})_{p}$ は部分和
$\log\rho(41)_{p}=-8\log 2+\sum\frac{1}{k\cdot 16^{k}}k=1p\mathrm{t}\mathrm{r}_{\mathbb{C}}\pi(B^{k})$ .
を意味するものとします。
方、8 の字結び回訓空間の双素的体積は、
$\mathrm{V}\mathrm{o}\mathrm{l}(41)=2.0298832128\cdots$
となることが知られています。したがって、
$L^{2}$ -torsion のlogarithm の実際
の値は
$\log\rho(4_{1})=-\frac{1}{3\pi}\mathrm{V}\mathrm{o}\mathrm{l}(41)$
$=-0.215377298\cdots$
で与えられることになります。
表1: 8 の字結び目の
$L^{2}$-torsion の近似計算
例22 次に、三葉結び目
$3_{1}$ について考えます。これは$(3, 2)$ 型トーラス結
び目なので、前節の最後で述べたことから、
$L^{2}$ -torsion は1 になります。こ
こでは、L\"uck の公式を用いて数値的に近似計算を行ってみます。
9
表2: 三葉結び目の
$L^{2}$-torsion の近似計算
この場合も
$\pi_{1}(3_{1})$ の表示として、
$S^{1}$ 上の曲面束として得られるものを採
用します:
$\pi=\langle x,y, t|txt^{-1}y^{-}1=tyt^{-1-1}xy=1\rangle$.
このときFox 行列は、
で与えられます。先と同様に生成元
$t$ に関する列
(第3 列目)
を除いたもの
を
$A$ とすれば、この場合も$K=4$ ととれて、
$B=16-\mathrm{A}A^{*}$$=$
となり、
$L^{2}$-torsion は次式で与えられることになります:
$\log\rho(3_{1})=-8\log 2+\sum_{p=}\infty 1\frac{1}{p\cdot 16^{p}}\mathrm{t}\mathrm{r}_{\mathbb{C}}\pi(B^{p})$.
この公式を用いた数値実験の結果を表2 にまとめておきます。
$\ovalbox{\tt\small REJECT}$方、三葉結び目
$3_{1}$ の
$S^{3}$ における補空間の体積は
$0$ になることが知られ
ています。
10
3
