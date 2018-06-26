#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM 5
//各点の構造体
struct data{
    double x;//x座標
    double y;//y座標
};

//距離を計算する関数
double Distance(struct data n1,struct data n2){
    return sqrt((n1.x-n2.x)*(n1.x-n2.x)+(n1.y-n2.y)*(n1.y-n2.y));
}

double SUM(struct data d[]){
    int i;
    double s=0;
    for(i=0;i<NUM-1;i++){
        s+=Distance(d[i],d[i+1]);
    }
    return s;
}

int main(void){
    FILE *fp;
    char fname[] = "input_0.csv";//←＊＊＊コマンドラインから入力に直す＊＊＊
    double x,y,s;
    struct data d[NUM];
    int i=0;
    
    //ファイルを開く
    fp = fopen(fname,"r");
    if(fp == NULL){
        printf("%s file not open\n",fname);
        return -1;
    }else{
        printf("%s file opened\n",fname);
    }
    //各行の読み込み
    fscanf(fp,"%*s,%*s");//一行目を読み飛ばす
    while(fscanf(fp,"%lf,%lf",&x,&y)!=EOF){
        printf("%lf %lf\n",x,y);//確かめ用出力(あとで消す）
        d[i].x=x;//構造体に代入
        d[i].y=y;
        i++;
    }
    
    s=SUM(d);
    printf("%lf\n",s);
    
    
    
    
    fclose(fp);
    return 0;
}
