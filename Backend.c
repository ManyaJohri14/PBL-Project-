#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int token;
    char msg[256];
    char reply[256]; 
    struct Node* next;
};

struct Node* top = NULL;

void push(int t, char m[], char r[]) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    if(temp == NULL) return;
    
    temp->token = t;
    strcpy(temp->msg, m);
    strcpy(temp->reply, r);
    
    temp->next = top;
    top = temp;
}

void pop() {
    struct Node* temp;
    if(top == NULL) return;
    temp = top;
    top = top->next;
    free(temp);
}

int main() {
    FILE *fp;
    int t_val;
    char m_val[256];
    char r_val[256] = ""; 
    
    fp = fopen("transfer.txt", "r");
    if(fp != NULL) {
        if(fscanf(fp, "%d\n", &t_val) != EOF) {
            fgets(m_val, sizeof(m_val), fp);
            m_val[strcspn(m_val, "\n")] = 0;
            
            push(t_val, m_val, r_val);
        }
        fclose(fp);
        remove("transfer.txt");
    }
    return 0;
}
