
            .data
N:      .word 10    # The length of Array
A:      .word 9     # A[0] = 9
        .word 3     # A[1] = 3
        .word 12
        .word 7
        .word 23
        .word 1
        .word 23
        .word 43
        .word 54    # A[8] = 54
        .word 31    # A[9] = 31
main:
	or $8,$0,$0 # i = 0
	or $9,$0,$0 # j = 0
    or $14,$0,$0 # k = 0
    or $15,$0,$0 # index = 0
    or $18,$0,$0
    addi $18, $18, 1# 比較するための１を用意
	lw $10, N
	la $11, A # A's address

	or $12, $0,$0 # tmp

	
loop1:	beq $8, $10, loopend1
	addi $8, $8,1

	sub $9, $10,$8 # N-i がjに入っている
loop2:	beq $9, $8, loopend2 # $9はj,$8はi
loop3: beq $9, $14, loopend3  # j個目のAを参照すれば良いので、$9になるまで
# このループでAの参照するべきアドレスを計算する
    addi $14, $14,1 # インクリメント
    addi $15, $15,4 # インデックスを4個ずつ進める
loop3end
	lw $13, $15($11)# ここで$13にA[j]を入れたい
    addi $15, $15, 4 # j+1のインデックスにする
    lw $16, $15($11) # ＄16にA[j+1]が入っている
    or $15,$0,$0 # インデックスを初期化しておく

    # ここまででA[j]とA[j+1]が揃ったため、ここからは並び替えをしていく
    # if分岐をするところ
    slt $17, $15, $13
    # 上の文はもしA[j+1]の方が小さかったら$17が1になるという意味
    beq $18, $17, swap1
swap1:
    sw $13, $15($11) # A[j+1]にA[j]の値を保存する
    addi $15, $15, -4 # A[j+1]のアドレスを参照する$15をA[j]を参照するようにする
    sw $16, $15($11) # A[j]にA[j+1]の値を保存する

swap1end:
	j loop2
loop2end:
	j loop1
loop1end: