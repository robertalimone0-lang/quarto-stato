-- Shortcode {{< dato CODICE >}}: stampa il valore registrato in dati/fonti.yaml
-- nel formato italiano (virgola decimale, punto delle migliaia) con l'unita.
-- Opzioni: unita="no" omette l'unita. I valori con stato diverso da "verificato"
-- sono seguiti da "(da validare)".
local function formatta(v, dec)
  local s = string.format("%." .. dec .. "f", v)
  local intero, decimali = s:match("^(-?%d+)%.?(%d*)$")
  local segno = ""
  if intero:sub(1, 1) == "-" then segno = "−"; intero = intero:sub(2) end
  local conmigliaia = intero:reverse():gsub("(%d%d%d)", "%1."):reverse()
  if conmigliaia:sub(1, 1) == "." then conmigliaia = conmigliaia:sub(2) end
  if decimali ~= "" then return segno .. conmigliaia .. "," .. decimali end
  return segno .. conmigliaia
end

return {
  ["dato"] = function(args, kwargs, meta)
    local codice = pandoc.utils.stringify(args[1])
    local voce = meta.fonti and meta.fonti[codice]
    if not voce then
      quarto.log.warning("dato mancante in fonti.yaml: " .. codice)
      return pandoc.Strong(pandoc.Str("[DATO MANCANTE: " .. codice .. "]"))
    end
    local v = tonumber(pandoc.utils.stringify(voce.valore))
    local dec = tonumber(pandoc.utils.stringify(voce.decimali or "0")) or 0
    local testo = formatta(v, dec)
    if pandoc.utils.stringify(kwargs["unita"] or "") ~= "no" and voce.unita then
      local u = pandoc.utils.stringify(voce.unita)
      if u == "%" or u:sub(1, 1) == "%" then testo = testo .. u else testo = testo .. " " .. u end
    end
    if pandoc.utils.stringify(voce.stato or "") ~= "verificato" then
      testo = testo .. " (da validare)"
    end
    return pandoc.Str(testo)
  end
}
