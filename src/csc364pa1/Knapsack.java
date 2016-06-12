package csc364pa1;

import java.util.Arrays;

/**
 * Created by pridemai on 6/12/16.
 */
public class Knapsack {
    public static void main(String[] args) {
        int[] objectValues={30,14,16,9};
        int[] objectWeights={6,3,4,2};
        int maxWeight = 10;
        int numberOfValues = 4;
        int[][] K = new int[numberOfValues+1][maxWeight+1];
        //fill up K
        for (int i =0; i <numberOfValues+1; i++){
            int[] tmp = new int[maxWeight+1];
            Arrays.fill(tmp, 0);
            K[i] =  tmp;
        }

        for (int j =0; j < numberOfValues+1; j++){
            for (int w=0; w< maxWeight+1;w++){
                if (j==0||w==0){
                    K[j][w] = 0;
                }
                else if(objectWeights[j-1] <= w){
                    K[j][w] = Math.max(K[j-1][w-objectWeights[j-1]]+objectValues[j-1],  K[j-1][w]);
                }
                else {
                    K[j][w] = K[j-1][w];
                }
            }

        }

        System.out.println(K[numberOfValues][maxWeight]);




    }
}
