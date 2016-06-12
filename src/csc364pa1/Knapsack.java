package csc364pa1;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
/**
 * Created by pridemai on 6/12/16.
 */
public class Knapsack {
    public static void main(String[] args) {
        /*
        Enter the number of available employee work weeks: 10
Enter the name of input file: KnapsackData1.txt
Enter the name of output file: Output1.txt

        Number of projects available: 4
Available employee work weeks: 10
Number of projects chosen: 2
Total profit: 46
Project0 6 30
Project2 4 16
        */
        String inputFile = "";
        String outputFile = "";
        System.out.println("Enter the input file: ");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            inputFile = br.readLine();
        } catch (IOException e) {
            System.exit(-1);
        }
        System.out.println("Enter the output file: ");
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            outputFile = br.readLine();
        } catch (IOException e) {
            System.exit(-1);
        }


        ArrayList<Integer> objectValues = new ArrayList<Integer>();
        ArrayList<String> projects = new ArrayList<String>();
        ArrayList<Integer> objectWeights = new ArrayList<Integer>();
        Scanner scan = null;
        try {
            scan = new Scanner(new File(inputFile));
        } catch (FileNotFoundException e) {
            System.exit(-1);
        }
        while(scan.hasNextLine()){
            String line = scan.nextLine();
            objectValues.add(Integer.parseInt(line.split(" ")[2]));
            objectWeights.add(Integer.parseInt(line.split(" ")[1]));
            projects.add(line.split(" ")[0]);

        }

        System.out.println("Enter the available number of weeks: ");
        int maxWeight = 0;
        try {
            maxWeight = Integer.parseInt(br.readLine());
        } catch (IOException e) {
            System.exit(-1);
        }
        int numberOfValues = objectValues.size();
        int[][] K = new int[numberOfValues+1][maxWeight+1];
        //fill up K
        for (int i =0; i <numberOfValues+1; i++){
            int[] tmp = new int[maxWeight+1];
            Arrays.fill(tmp, 0);
            K[i] =  tmp;
        }
        //iterate n^2
        for (int j =0; j < numberOfValues+1; j++){
            for (int w=0; w< maxWeight+1;w++){
                if (j==0||w==0){
                    K[j][w] = 0;
                }
                else if(objectWeights.get(j-1) <= w){
                    K[j][w] = Math.max(K[j-1][w-objectWeights.get(j-1)]+objectValues.get(j-1),  K[j-1][w]);
                }
                else {
                    K[j][w] = K[j-1][w];
                }
            }

        }

        //so now we get the number of items used n...1

        ArrayList<Integer> usedProjects = new ArrayList<Integer>();
        int tmpWeight =maxWeight;
        for (int i  = numberOfValues; i > 0; i--){
            int itemWeight = objectWeights.get(i-1);
            if (K[i][tmpWeight] == K[i-1][tmpWeight]){
                continue;
            }else{
                usedProjects.add(i-1);
                tmpWeight = tmpWeight-itemWeight;

            }

        }


        String output = "Number of projects available: " +projects.size()+"\nAvailable employee work weeks: "+maxWeight+"" +
                "\nNumber of projects chosen: "+usedProjects.size()+"\nTotal Profit: "+K[numberOfValues][maxWeight]+"\n\n";
        System.out.print(output);
        for (int i =0; i < usedProjects.size(); i++){
            System.out.println(projects.get(usedProjects.get(i))+" "+objectValues.get(usedProjects.get(i)));
        }

//        System.out.println("Total items: "+totalItems+"\nTotal value: "+K[numberOfValues][maxWeight]);




    }
}
