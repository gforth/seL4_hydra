.text
.global __set_thread_area
.type   __set_thread_area,@function
__set_thread_area:
	push %ebx
	push $0x51
	push $0xfffff
	push 16(%esp)
	push $-1
	mov %esp,%ebx
	xor %eax,%eax
	mov $243,%al
	int $128
	testl %eax,%eax
	jnz 2f
	movl (%esp),%edx
	leal 3(,%edx,8),%edx
3:	movw %dx,%gs
1:
	addl $16,%esp
	popl %ebx
	ret
2:
	mov %ebx,%ecx
	xor %ebx,%ebx
	xor %edx,%edx
	mov %ebx,(%esp)
	mov $1,%bl
	mov $16,%dl
	mov $123,%al
	int $128
	testl %eax,%eax
	jnz 1b
	mov $7,%dl
	inc %al
	jmp 3b
