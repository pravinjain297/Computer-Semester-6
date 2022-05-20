/*
Lab Assignment No: 03

Problem Statement: ImplementGreedy Search Algorithm for any one of the following application:
                   I. Selection Sort
*/

#include <iostream>
using namespace std;


void display_array(int *arr, int size)              // Function to print array
{
    for(int i=0; i<size; i++)
        cout<<arr[i]<<" ";
}

void selection_sort(int *arr, int size)             // Function for Selection Sort 
{
    int i,j,min_ele,temp;

    for(i=0;i<size;i++)
    {
        min_ele=i;
        
        for(j=i+1; j<size; j++)
        {
            if(arr[j] < arr[min_ele])		    // compare min_ele with others element of list & if element is small than min_ele then store in min_ele.
                min_ele=j;
        }
        
        temp=arr[i];                                //Swapping of element in list
        arr[i]=arr[min_ele];
        arr[min_ele]=temp;
    }
}

int main()
{
    
    int no_ele, arr[10];
    cout<<"\n----------------------- Selection Sort -----------------------\n";
    
    cout<<"\nEnter the no. of elements to sort: ";
    cin>>no_ele;
    
    cout<<"\nEnter "<<no_ele<<" elements of array to sort: \n";
    for(int i=0; i<no_ele; i++)
        cin>>arr[i];
        
    cout<<"\nArray before sorting is: \n";
    display_array(arr,no_ele);
        
    selection_sort(arr,no_ele);
    
    cout<<"\nArray After sorting is: \n";
    display_array(arr,no_ele);
    
    return 0;
}

/* Output:

----------------------- Selection Sort -----------------------

Enter the no. of elements to sort: 5

Enter 5 elements of array to sort: 
12
3
10
2
5

Array before sorting is: 
12 3 10 2 5 
Array After sorting is: 
2 3 5 10 12 
*/