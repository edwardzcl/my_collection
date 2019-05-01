//以下这段代码参考自：https://blog.csdn.net/qq_21808961/article/details/78213326

/*这段代码编译会报错，可能以前老版本，不太严格的编译器上可能不会报错，甚至还能运行。。
但是像现在的MSVS2015上就在编译就不会通过，对两边指针的类型要求格外严格
*/


/**
通过指针来访问一维数组，二维数组，多维数组
*/
 
#include<stdio.h>
const int COLS=3;
const int COUNT=4;
//通过一级指针，计算偏移量来遍历一维数组
void printSingleDimensionalArray(int *data,int data_len);
//通过一级指针，计算偏移量来遍历二维数组:
void printDoubleDimensionalArray(int *array,int rows,int cols);
//通过一级指针，计算偏移量来遍历三维数组:
void printThreeDimensionalArray(int *array_3,int rows,int cols,int count);
//使用指向二维数组的指针来遍历三维数组
void printThreeDimensionalArray2(int (*p)[COLS][COUNT],int rows);
 
void main()
{
    int data[]={1,2,3,4,5,6,7,8,9};
    int data_len=sizeof(data)/sizeof(data[0]);
    printf("data[6]=%d\n",*(data+6));//7
    printf("一维数组data:\n");
    printSingleDimensionalArray(data,data_len);
    int array[2][3]={{1,2,3},{4,5,6}};
    printf("二维数组array：\n");
    printDoubleDimensionalArray(array,2,3);
    int count=0;
    int array_3[2][3][4];
    int i,j,k;
    for(i=0;i<2;i++)
    {
        for(j=0;j<3;j++)
        {
            for(k=0;k<4;k++)
            {
 
                array_3[i][j][k]=count++;
            }
 
        }
    }
    printf("三维数组array_3:\n");
    printThreeDimensionalArray(array_3,2,3,4);
    //三维数组的初始化
    int array_33[2][3][4]=
    {
        {
            {1,2,3,4},
            {5,6,7,8},
            {9,10,11,12},
        },
        {
            {13,14,15,16},
            {17,18,19,20},
            {21,22,23,24},
        }
    };
    printf("三维数组array_33:\n");
    printThreeDimensionalArray(array_33,2,3,4);
    printf("三维数组array_33:\n");
    printThreeDimensionalArray2(array_33,2);
}
//通过一级指针，计算偏移量来遍历一维数组
void printSingleDimensionalArray(int *data,int data_len)
{
    int i;
    for(i=0;i<data_len;i++)
        printf("%4d",*(data+i));//7
    printf("\n");
}
//通过一级指针，计算偏移量来遍历二维数组:
void printDoubleDimensionalArray(int *array,int rows,int cols)
{
    int i,j;
    for(i=0;i<rows;i++)
    {
        for(j=0;j<cols;j++)
        {//通过一位指针，计算偏移量来遍历二维数组:
            printf("%4d",*(array+i*cols+j));
        }
        printf("\n");
    }
}
//通过一级指针，计算偏移量来遍历三维数组:
void printThreeDimensionalArray(int *array_3,int rows,int cols,int count)
{
    int i,j,k;
    for(i=0;i<rows;i++)
    {
        printf("{\n");
        for(j=0;j<cols;j++)
        {
            for(k=0;k<count;k++)
            {
 
//                array[i][j][k]=count++;
//                printf("%4d",array_3[i][j][k]);
                printf("%4d",*(array_3+i*3*4+j*4+k));
            }
            printf("\n");
        }
        printf("}\n");
    }
}
//使用指向二维数组的指针来遍历三维数组
void printThreeDimensionalArray2(int (*p)[COLS][COUNT],int rows)
{
    int i,j,k;
    for(i=0;i<rows;i++)
    {
        printf("{\n");
        for(j=0;j<COLS;j++)
        {
            for(k=0;k<COUNT;k++)
            {
 
//                array[i][j][k]=count++;
                printf("%4d",p[i][j][k]);
//                printf("%4d",*(array_3+i*3*4+j*4+k));
            }
            printf("\n");
        }
        printf("}\n");
    }




//第二段代码，来源未知
#include <stdio.h>

int main(void)

{

	int *p = NULL;
	int a[2][3] = { {1,2,3},{2,3,4} };
	p = a;
	printf("%d",*(*(p + 1) + 1));

	return 0;

}

//第三段代码，来源未知

#include <stdio.h>

int main(void)

{

	int **p = NULL;
	int a[2][3] = { {1,2,3},{2,3,4} };
	p = a;
	printf("%d",*(*(p + 1) + 1));

	return 0;

}


//第四段代码，来源未知
#include <stdio.h>

int main(void)

{

	int **p = NULL;
	int a[2][3] = { {1,2,3},{2,3,4} };
	//p = a;
	printf("%d",*(*(a + 1) + 1));

	return 0;

}


//第五段代码，来源未知
#include <stdio.h>

int main(void)

{

	int **p = NULL;
	int a[i][j];
	p = a;
	a[i][j] = *(*(p + i) + j);

	return 0;

}


//第六段代码，来源未知
#include <stdio.h>

int main(void)

{

	int a[2][4] = { { 2,5,6,8 },{ 22,55,66,88 } };

	int c[4] = { 5,8,9,4 };

	int d[3] = { 23,12,443 };

	int *p[4], (*q)[4];

	q = a;

	p[0] = c;

	p[1] = d;

	int i, j;

	for (i = 0; i<2; i++)

		for (j = 0; j<4; j++)

		{

			if ((i == 1) && (j == 3)) break;

			printf("*(*(p+%d)+%d)=%d\n", i, j, *(*(p + i) + j));

		}

	puts("===============");

	for (i = 0; i<2; i++)

		for (j = 0; j<4; j++)

			printf("*(*(q+%d)+%d)=%d\n", i, j, *(*(q + i) + j));

	return 0;


//第七段代码，来源未知
#include <stdio.h>

int main(void)

{

	int a[2][4] = { { 2,5,6,8 },{ 22,55,66,88 } };

	int c[4] = { 5,8,9,4 };

	int d[3] = { 23,12,443 };

	int *p[4], (*q)[4];

	q = a;

	*p = c;

	*(p + 1) = d;

	int i, j;

	for (i = 0; i<2; i++)

		for (j = 0; j<4; j++)

		{

			if ((i == 1) && (j == 3)) break;

			printf("*(*(p+%d)+%d)=%d\n", i, j, *(*(p + i) + j));

		}

	puts("===============");

	for (i = 0; i<2; i++)

		for (j = 0; j<4; j++)

			printf("*(*(q+%d)+%d)=%d\n", i, j, *(*(q + i) + j));

	return 0;

}

//第八段代码，来源未知
#include <string.h>

void Exchg1(int x, int y)   //定义中的x,y变量被称为Exchg1函数的形式参数
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	printf("x = %d, y = %d \n", x, y);
}

void main()
{
	int a = 4, b = 6, &aa=a, &bb=b;
	Exchg1(aa, bb);     //a,b变量为Exchg1函数的实际参数。
	printf("a = %d, b = %d \n", a, b);



}


//第九段代码，来源未知

#include <stdio.h>
#include <string.h>

void Exchg1(int &x, int &y)   //定义中的x,y变量被称为Exchg1函数的形式参数
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	printf("x = %d, y = %d \n", x, y);
}

void main()
{
	int a = 4, b = 6, &aa=a, &bb=b;
	Exchg1(aa, bb);     //a,b变量为Exchg1函数的实际参数。
	printf("a = %d, b = %d \n", a, b);



}


//第十段代码，来源未知
#include <stdio.h>
#include <string.h>

void Exchg1(int &x, int &y)   //定义中的x,y变量被称为Exchg1函数的形式参数
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	printf("x = %d, y = %d \n", x, y);
}

void main()
{
	int a = 4, b = 6, &aa=a, &bb=b;
	Exchg1(a, b);     //a,b变量为Exchg1函数的实际参数。
	printf("a = %d, b = %d \n", a, b);



}


//第十一段代码，来源未知

#include <stdio.h>
#include <string.h>

void Exchg1(int x, int y)   //定义中的x,y变量被称为Exchg1函数的形式参数
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	printf("x = %d, y = %d \n", x, y);
}

void main()
{
	int a = 4, b = 6, &aa=a, &bb=b;
	Exchg1(a, b);     //a,b变量为Exchg1函数的实际参数。
	printf("a = %d, b = %d \n", a, b);



}


//第十二段代码，来源未知
#include <stdio.h>
#include <string.h>

void Exchg1(int x, int y)   //定义中的x,y变量被称为Exchg1函数的形式参数
{
	int tmp;
	tmp = x;
	x = y;
	y = tmp;
	printf("x = %d, y = %d \n", x, y);
}

void main()
{
	int a = 4, b = 6, &aa=a, &bb=b;
	Exchg1(a, b);     //a,b变量为Exchg1函数的实际参数。
	printf("a = %d, b = %d \n", a, b);



}


//第十三段代码，来源未知

#include <stdio.h>
#include <string.h>

char * fun(char * p1, char * p2)
{
	int i = 0;
	i = strcmp(p1, p2);

	if (0 == i)
	{
		return p1;
	}
	else
	{
		return p2;
	}
}

int main()
{
	char b[] = "lemon";//创建于栈区
	char *q = b;//等同于 char *q=&b[0]
	char *qq = &b[1];

	printf("sizeof(b)=%d  strlen(b)=%d\n", sizeof(b), strlen(b));//6  5

	printf("q1=%p\n", q);//输出16进制地址值
	printf("q2=%d\n", q);//输出10进制形式的地址值
	printf("q3=%s\n", q);//输出字符串
	printf("q4=%c\n", *q);//输出字符

	printf("b[0]=%c\n", b[0]);//输出字符l

	printf("qq1=%c\n", *qq);//输出字符
	printf("qq2=%s\n", qq);//输出字符串
	printf("qq4=%d\n", qq);//没有*，输出指针的地址值的10进制形式
	printf("qq3=%d\n", *qq);//有*，输出指针所指内容（e）,但%d要求输出整型，故输出e的ASCII码


	for (int i = 0; i < 5; i++)
	{
		char *t = q + i;
		printf("%c  %s\n", *t, t);
		*t = 'a';//更改b
	}
	printf("%s", b);//aaaaa

	return 0;
}


//第十四段代码，来源未知
#include <stdio.h>
#include <string.h>

char * fun(char * p1, char * p2)
{
	int i = 0;
	i = strcmp(p1, p2);

	if (0 == i)
	{
		return p1;
	}
	else
	{
		return p2;
	}
}

int main()
{
	char b[] = "lemon";//创建于栈区
	char *q = b;//等同于 char *q=&b[0]
	char *qq = &b[0];

	printf("sizeof(b)=%d  strlen(b)=%d\n", sizeof(b), strlen(b));//6  5

	printf("q1=%p\n", q);//输出16进制地址值
	printf("q2=%d\n", q);//输出10进制形式的地址值
	printf("q3=%s\n", q);//输出字符串
	printf("q4=%c\n", *q);//输出字符

	printf("b[0]=%c\n", b[0]);//输出字符l

	printf("qq1=%c\n", *qq);//输出字符
	printf("qq2=%s\n", qq);//输出字符串
	printf("qq4=%d\n", qq);//没有*，输出指针的地址值的10进制形式
	printf("qq3=%d\n", *qq);//有*，输出指针所指内容（e）,但%d要求输出整型，故输出e的ASCII码


	for (int i = 0; i < 5; i++)
	{
		char *t = qq + i;
		printf("%c  %s\n", *t, t);
		*t = 'a';//更改b
	}
	printf("%s", b);//aaaaa

	return 0;
}


//第十五段代码，来源未知
#include<string.h>
#include <stdio.h>
void Function()
{
	printf("Call Function!\n");
}
int main()
{
	void(*p)();
	*(int*)&p = (int)Function;
	(*p)();



	int *a[3];
	int *(*b)[3] = &a;

	int *c[3];
	int **d = c;

	int *e[3];
	int *(*f) = e;

	int n[2][3][4];
	int *q[3][2];
	int *(*l)[3][2] = &q;

	char h[5] = { 'a','b','c','d' };
	char(*p1)[5] = &h;
	char(*p2)[5] = (char(*)[5])h;

	printf("a=%d\n", h);
	printf("a=%c\n", h[0]);
	printf("p1=%c\n", **p1);
	printf("p2=%c\n", **p2);
	printf("p1+1=%c\n", **(p1 + 1));
	printf("p2+1=%c\n", **(p2 + 1));

	return 0;

}


/*更多请参考我的博客：
https://www.cnblogs.com/li-peng/p/4116349.html
https://www.cnblogs.com/qquan/articles/4940043.html
https://www.cnblogs.com/mq0036/p/3382732.html
https://blog.csdn.net/edward_zcl/article/details/89345096
https://blog.csdn.net/edward_zcl/article/details/89451078

