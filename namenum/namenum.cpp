
/*
ID: araoudu1
PROG: namenum
LANG: C++
*/
#include <fstream>  // used to create a file object
#include <string>   // used to create strings
#include <map>      // used to create a dict
#include <iostream> // Used to print things

using namespace std;

map<char, char> mp;

int main()
{
    mp['A'] = mp['B'] = mp['C'] = '2';
    mp['D'] = mp['E'] = mp['F'] = '3';
    mp['G'] = mp['H'] = mp['I'] = '4';
    mp['J'] = mp['K'] = mp['L'] = '5';
    mp['M'] = mp['N'] = mp['O'] = '6';
    mp['P'] = mp['R'] = mp['S'] = '7';
    mp['T'] = mp['U'] = mp['V'] = '8';
    mp['W'] = mp['X'] = mp['Y'] = '9';

    string digits;
    ifstream fin("namenum.in");
    ofstream fout("namenum.out");
    ifstream fulldict("dict.txt");
    fin >> digits;

    string currentword;
    bool hasAtleastOneValidWord = false;
    while (fulldict >> currentword)
    {
        if (currentword.size() != digits.size())
            continue;
        bool valid = true;
        for (int i = 0; i < currentword.size(); i++)
            if (mp[currentword[i]] != digits[i])
            {
                cout << mp[currentword[i]] << digits[i] << endl;
                valid = false;
                break;
            }
        if (valid)
        {
            hasAtleastOneValidWord = true;
            fout << currentword << endl;
        }
    }

    if (!hasAtleastOneValidWord)
    {
        fout << "NONE" << endl;
    }
    return 0;
}