class Encode_Decode:
    def encode(self,str_list):
        res=""
        for s in str_list:
            res+=str(len(s))+"#"+s
        return res
    
    def decode (self,string):
        res,i=[],0
        while i < len(string):
            j=i
            while string[j]!='#':
                j+=1
            length=int(string[i:j])
            res.append(string[j+1:j+1+length])
            i=j+1+length
        return res

string_list=["hello","bye"]
obj=Encode_Decode()
encoded_string=obj.encode(string_list)
print(encoded_string)
print(obj.decode(encoded_string))