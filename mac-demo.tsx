"use client"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Textarea } from "@/components/ui/textarea"
import { AlertCircle, CheckCircle, Eye, EyeOff, Hash, Key } from "lucide-react"
import { useState } from "react"

// Simple HMAC implementation for demo purposes
function simpleHMAC(key: string, message: string): string {
  // This is a simplified version for educational purposes
  const keyBytes = new TextEncoder().encode(key)
  const messageBytes = new TextEncoder().encode(message)

  // Simple hash function (not cryptographically secure)
  let hash = 0
  const combined = key + message
  for (let i = 0; i < combined.length; i++) {
    const char = combined.charCodeAt(i)
    hash = (hash << 5) - hash + char
    hash = hash & hash // Convert to 32-bit integer
  }

  return Math.abs(hash).toString(16).padStart(8, "0")
}

// USAC simulation (simplified)
function generateUSAC(message: string, key: string): string {
  // Simplified USAC implementation
  const messageLength = message.length
  const keyLength = key.length

  if (keyLength < messageLength) {
    throw new Error("USAC requires key length >= message length")
  }

  let result = ""
  for (let i = 0; i < messageLength; i++) {
    const messageChar = message.charCodeAt(i)
    const keyChar = key.charCodeAt(i)
    const xor = messageChar ^ keyChar
    result += xor.toString(16).padStart(2, "0")
  }

  return result
}

export default function CryptoMACDemo() {
  const [macMessage, setMacMessage] = useState("")
  const [macKey, setMacKey] = useState("")
  const [macResult, setMacResult] = useState("")
  const [macVerifyResult, setMacVerifyResult] = useState("")
  const [macVerifyStatus, setMacVerifyStatus] = useState<"none" | "valid" | "invalid">("none")

  const [usacMessage, setUsacMessage] = useState("")
  const [usacKey, setUsacKey] = useState("")
  const [usacResult, setUsacResult] = useState("")
  const [usacError, setUsacError] = useState("")
  const [showKey, setShowKey] = useState(false)

  const generateMAC = () => {
    if (!macMessage || !macKey) return
    const result = simpleHMAC(macKey, macMessage)
    setMacResult(result)
  }

  const verifyMAC = () => {
    if (!macMessage || !macKey || !macVerifyResult) return
    const expectedMAC = simpleHMAC(macKey, macMessage)
    setMacVerifyStatus(expectedMAC === macVerifyResult ? "valid" : "invalid")
  }

  const generateUSACCode = () => {
    try {
      setUsacError("")
      if (!usacMessage || !usacKey) return
      const result = generateUSAC(usacMessage, usacKey)
      setUsacResult(result)
    } catch (error) {
      setUsacError(error instanceof Error ? error.message : "Unknown error")
      setUsacResult("")
    }
  }

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      <div className="text-center space-y-2">
        <h1 className="text-3xl font-bold">Kriptografi: MAC & USAC Demo</h1>
        <p className="text-muted-foreground">
          Demonstrasi Message Authentication Code dan Unconditional Secure Authentication Code
        </p>
      </div>

      <Tabs defaultValue="mac" className="w-full">
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="mac">MAC Demo</TabsTrigger>
          <TabsTrigger value="usac">USAC Demo</TabsTrigger>
          <TabsTrigger value="comparison">Perbandingan</TabsTrigger>
        </TabsList>

        <TabsContent value="mac" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Hash className="h-5 w-5" />
                Message Authentication Code (MAC)
              </CardTitle>
              <CardDescription>
                Generate dan verifikasi MAC untuk memastikan integritas dan autentisitas pesan
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="mac-message">Pesan</Label>
                  <Textarea
                    id="mac-message"
                    placeholder="Masukkan pesan yang akan di-MAC..."
                    value={macMessage}
                    onChange={(e) => setMacMessage(e.target.value)}
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="mac-key">Kunci Rahasia</Label>
                  <div className="relative">
                    <Input
                      id="mac-key"
                      type={showKey ? "text" : "password"}
                      placeholder="Masukkan kunci rahasia..."
                      value={macKey}
                      onChange={(e) => setMacKey(e.target.value)}
                    />
                    <Button
                      type="button"
                      variant="ghost"
                      size="icon"
                      className="absolute right-0 top-0 h-full px-3 py-2 hover:bg-transparent"
                      onClick={() => setShowKey(!showKey)}
                    >
                      {showKey ? (
                        <EyeOff className="h-4 w-4 text-muted-foreground" />
                      ) : (
                        <Eye className="h-4 w-4 text-muted-foreground" />
                      )}
                    </Button>
                  </div>
                </div>
              </div>

              <Button onClick={generateMAC} className="w-full">
                Generate MAC
              </Button>

              {macResult && (
                <div className="space-y-2">
                  <Label>MAC Result:</Label>
                  <div className="p-3 bg-muted rounded-md font-mono text-sm break-all">{macResult}</div>
                </div>
              )}

              <div className="border-t pt-4">
                <h4 className="font-semibold mb-2">Verifikasi MAC</h4>
                <div className="space-y-2">
                  <Label htmlFor="mac-verify">MAC untuk Verifikasi</Label>
                  <Input
                    id="mac-verify"
                    placeholder="Masukkan MAC yang akan diverifikasi..."
                    value={macVerifyResult}
                    onChange={(e) => setMacVerifyResult(e.target.value)}
                  />
                  <Button onClick={verifyMAC} variant="outline" className="w-full">
                    Verifikasi MAC
                  </Button>

                  {macVerifyStatus !== "none" && (
                    <div className="flex items-center gap-2">
                      {macVerifyStatus === "valid" ? (
                        <>
                          <CheckCircle className="h-4 w-4 text-green-500" />
                          <Badge variant="default" className="bg-green-500">
                            Valid
                          </Badge>
                          <span className="text-sm text-green-600">MAC valid - Pesan autentik</span>
                        </>
                      ) : (
                        <>
                          <AlertCircle className="h-4 w-4 text-red-500" />
                          <Badge variant="destructive">Invalid</Badge>
                          <span className="text-sm text-red-600">MAC tidak valid - Pesan mungkin diubah</span>
                        </>
                      )}
                    </div>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="usac" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Key className="h-5 w-5" />
                Unconditional Secure Authentication Code (USAC)
              </CardTitle>
              <CardDescription>
                Generate USAC dengan keamanan tanpa syarat (information-theoretic security)
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="bg-yellow-50 border border-yellow-200 rounded-md p-3">
                <p className="text-sm text-yellow-800">
                  <strong>Catatan:</strong> USAC memerlukan kunci dengan panjang minimal sama dengan pesan untuk
                  keamanan optimal.
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="usac-message">Pesan</Label>
                  <Textarea
                    id="usac-message"
                    placeholder="Masukkan pesan..."
                    value={usacMessage}
                    onChange={(e) => setUsacMessage(e.target.value)}
                  />
                  <p className="text-xs text-muted-foreground">Panjang: {usacMessage.length} karakter</p>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="usac-key">Kunci (One-Time Pad)</Label>
                  <Textarea
                    id="usac-key"
                    placeholder="Masukkan kunci (harus >= panjang pesan)..."
                    value={usacKey}
                    onChange={(e) => setUsacKey(e.target.value)}
                  />
                  <p className="text-xs text-muted-foreground">Panjang: {usacKey.length} karakter</p>
                </div>
              </div>

              <Button onClick={generateUSACCode} className="w-full">
                Generate USAC
              </Button>

              {usacError && (
                <div className="flex items-center gap-2 p-3 bg-red-50 border border-red-200 rounded-md">
                  <AlertCircle className="h-4 w-4 text-red-500" />
                  <span className="text-sm text-red-600">{usacError}</span>
                </div>
              )}

              {usacResult && (
                <div className="space-y-2">
                  <Label>USAC Result:</Label>
                  <div className="p-3 bg-muted rounded-md font-mono text-sm break-all">{usacResult}</div>
                  <p className="text-xs text-muted-foreground">Hasil enkripsi XOR antara pesan dan kunci</p>
                </div>
              )}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="comparison" className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <Card>
              <CardHeader>
                <CardTitle>Message Authentication Code (MAC)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div>
                  <h4 className="font-semibold text-sm">Keamanan:</h4>
                  <p className="text-sm text-muted-foreground">Computational security</p>
                </div>
                <div>
                  <h4 className="font-semibold text-sm">Kunci:</h4>
                  <p className="text-sm text-muted-foreground">Kunci tetap, dapat digunakan berulang</p>
                </div>
                <div>
                  <h4 className="font-semibold text-sm">Efisiensi:</h4>
                  <p className="text-sm text-muted-foreground">Sangat efisien, cocok untuk aplikasi praktis</p>
                </div>
                <div>
                  <h4 className="font-semibold text-sm">Penggunaan:</h4>
                  <p className="text-sm text-muted-foreground">TLS, IPSec, SSH, aplikasi web</p>
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Unconditional Secure Authentication Code (USAC)</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div>
                  <h4 className="font-semibold text-sm">Keamanan:</h4>
                  <p className="text-sm text-muted-foreground">Information-theoretic security</p>
                </div>
                <div>
                  <h4 className="font-semibold text-sm">Kunci:</h4>
                  <p className="text-sm text-muted-foreground">One-time pad, panjang ≥ pesan</p>
                </div>
                <div>
                  <h4 className="font-semibold text-sm">Efisiensi:</h4>
                  <p className="text-sm text-muted-foreground">Kurang efisien, memerlukan manajemen kunci kompleks</p>
                </div>
                <div>
                  <h4 className="font-semibold text-sm">Penggunaan:</h4>
                  <p className="text-sm text-muted-foreground">Aplikasi militer, komunikasi high-security</p>
                </div>
              </CardContent>
            </Card>
          </div>

          <Card>
            <CardHeader>
              <CardTitle>Perbedaan Sebelum dan Setelah Penerapan</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div>
                  <h4 className="font-semibold">Sebelum Penerapan:</h4>
                  <ul className="list-disc list-inside text-sm text-muted-foreground space-y-1">
                    <li>Pesan dapat diubah tanpa deteksi</li>
                    <li>Tidak ada jaminan autentisitas pengirim</li>
                    <li>Rentan terhadap man-in-the-middle attacks</li>
                    <li>Tidak ada mekanisme verifikasi integritas</li>
                  </ul>
                </div>
                <div>
                  <h4 className="font-semibold">Setelah Penerapan:</h4>
                  <ul className="list-disc list-inside text-sm text-muted-foreground space-y-1">
                    <li>Perubahan pesan dapat terdeteksi</li>
                    <li>Autentisitas pengirim terjamin</li>
                    <li>Perlindungan terhadap replay attacks</li>
                    <li>Integritas data terjaga selama transmisi</li>
                  </ul>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}
