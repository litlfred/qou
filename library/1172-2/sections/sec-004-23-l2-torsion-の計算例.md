---
doc_id: 1172-2
doc_title: "$L^{2}$-torsion of 3-manifolds 北野晃朗* (東京工業大学) (東京工業大学) 森藤孝之\dagger (東京大学) 2000 年7 月 はじめに. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . お礼の言葉"
section_id: sec-004-23-l2-torsion-の計算例
section_title: "$L^{2}$-torsion の計算例"
section_number: 2.3
pages: 8-13
source_pdf: 1172-2.pdf
source_sha256: 390665341d5b7522
toc_source: inferred
---
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
15
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
16
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
17
3
$S^{1}$ 上の曲面束の
$L^{2}$-torsion
この章では、
$S^{1}$ 上の1 つ境界を持った曲面束を考えます。すなわち、
$\Sigma_{g,1}$
を種数$g\geq 1$ の向き付けられたコンパクトな曲面(実2 次元多様体) で境界を
–つ持つものとします。ここで、
$\varphi$ :
$\Sigma_{g,1}arrow\Sigma_{g,1}$
を
$\Sigma_{g,1}$ 上の向きを保つ微分同相写像とします。この写像
$\varphi$ のmapping torus
を
$W_{\varphi}$ と書きます。このトーラスを境界に持つ3 次元多様体
$W_{\varphi}$ には、自然
な射影
$W_{\varphi}arrow S^{1}$ が存在し、
$S^{1}$ 上の
$\Sigma_{g,1}$ 束の構造が入ります。以下簡単の
ため、
$\pi:=\pi_{1}(W_{\varphi}, *)$ ,
$\Gamma:=\pi_{1}(\Sigma_{\mathit{9},1}, *)$
とします。但し、
$\pi$ と
$\Gamma$ の基点
$*$ は
$\Sigma_{g,1}\cross\{0\}\subset W_{\varphi}$ 上の同–の点とします。
この時、
$\pi$ は
$\Gamma$ と
$\mathbb{Z}\cong\langle t\rangle$ の半直積と同型になります。
注意3.1
$\varphi$ が擬アノソフ微分同相写像であれば、
$W_{\varphi}$ の内部はトーラスカス
プを持つ完備な双曲的多様体となることが知られています。
ここで、$B(l^{2}(\pi), \iota^{2}(\pi))^{\pi}$ を
$\pi-$同変な
$l^{2}(\pi)$ 上の有界線形作用素の全体とし
ます。前の章では基本群
$\pi$ の右正則表現
$\piarrow B(l^{2}(\pi), \iota^{2}(\pi))^{\pi}$
を考え、それを使ってヒルベルト加群係数のねじれホモロジーを考えて
$L^{2}-$
torsion
$\rho(W_{\varphi})$ を定義しました。
以下では
$l^{2}(\pi)$ を
$\Gamma$ の暗中遷化列を使って近似することを考え、それによっ
て、元々の
$L^{2}$-torsion
$\rho(W_{\varphi})$ を近似する
$L^{2}$-torsion の列$\rho_{k}(W_{\varphi})(k=1,2, \ldots)$
を構成する$-$つの試みに付いて述べます。
3.1
降中心化列から定まる
$L^{2}$-torsion
基本群
$\pi_{1}(\Sigma_{g,1})=\Gamma$ は、階数が
$2g$ の自由群です。そこで、自由群
$\Gamma$ の降
中心化列
$\Gamma_{1}$
$:=\Gamma\supset\Gamma_{2}\supset.$
$:$ .
$\supset\Gamma_{k}\supset.$ . .
11
18
を考えます。但し、$\Gamma_{2}:=[\Gamma_{1} , \Gamma_{1}]_{\text{、}}$
一般に$k>2$ に対して、$\Gamma_{k}:=[\Gamma k-1, \mathrm{r}1]$
です。さらに
$\Gamma$ の幕豪商
$\mathrm{M}$ :=F/Fk、そして、そこへの自然な射影$p_{k}$ :
$\Gammaarrow$
$N_{k}$ を考えます。
注意32 古典的に
$\Gamma$ は、剰余幕零性を持つことは知られています。すなわち
自明でない任意の元
$x\in\Gamma$ に対して、ある
$k$ が存在して$p_{k}(x)\neq e$ となりま
す。これらについては$[5, 13]$ を参照して下さい。
前の章では
$\pi$ の
$l^{2}(\pi)$ の上への正則表現を考えました。
$\Gamma_{k}$ は
$\pi$ の正規部
分群なので、その商群$\pi(k):=\pi/\Gamma_{k}$ を考える事ができます。そこで、
$\pi$ の
$l^{2}(\pi(\text{ん}))$ の上への表現、すなわち、
$\piarrow B(l^{2}(\pi(k)), \iota^{2}(\pi(k)))^{\pi}$
を考えましょう。この表現により、前の章と同様にして、3 次元多様体
$W_{\varphi}$ の
$L^{2}$-torsion
$\rho_{k}(W_{\varphi})$ が幾つかの仮定、すなわち、
$L^{2}$-ベッチ数の消滅とNovikov-
Shubin 不変量の正値性の下で定義されます。
補題3.1 上の表現$\piarrow B(l^{2}(\pi(k)), \iota^{2}(\pi(k)))^{\pi}$ で捻った
$W_{\varphi}$ のホモロジーは
全て消える。
証明の詳細は省略しますが、$k=1$ の時、
$l^{2}$ (Z)-係数ホモロジーが消えるこ
とが証明でき
([11] 参照のこと)、$k>1$ の場合はそこに帰着させることがで
きます。
Novikov-Shubin 不変量の正値性については以後仮定をして話を進めます。
注意33 以下で述べることは全て、Novikov-Shubin 不変量の正恒性が成り
立つと仮定すれば、数学的に正しい事が証明されます。しかし、その正値性
についてはある型のトーラス束の場合には証明されていますが、–般的には
未だ未解決と思われます。
注意34 正則表現をその他の無限次元表現に取り替えて
$L^{2}$-torsion を定義
した仕事はもともとCarey-Mathai [2] にあります。この論文ではL2-ベッチ
数が消滅し、Novikov-Shubin 不変量の正となる表現の事をadmissible 表現
と呼び、このような表現に対して
$L^{2}$-torsion を定義しています。
もともと基本群
$\pi\cong\Gamma\rangle\triangleleft \mathbb{Z}$ でした。よって、明らかに今の場合
$\pi(k)\cong$
$N_{k}\rangle\triangleleft \mathbb{Z}$ です。この事から、群の列
$\{\pi(k)\}$ は
$\Gamma$ の剰余三三性から素朴な意味
で
$\pi$ の近似列です。この近似列から定まる表現はもともとの正則表現
$\piarrow$
12
19
$B(l^{2}(\pi), \iota^{2}(\pi))^{\pi}$ の近似列と見なすことができます。よってこれから定まる
$L^{2}- \mathrm{t}_{\mathrm{o}\mathrm{r}}\mathrm{S}\mathrm{i}\mathrm{o}\mathrm{n}$ を考えれば、これは下の
$L^{2}$-torsion を近似しているはずです。具
