package com.kefu.mock.controller;

import com.kefu.mock.model.AfterSaleRequest;
import com.kefu.mock.repository.AfterSaleRepository;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/api/aftersale")
public class AfterSaleController {

    private final AfterSaleRepository afterSaleRepository;

    public AfterSaleController(AfterSaleRepository afterSaleRepository) {
        this.afterSaleRepository = afterSaleRepository;
    }

    @GetMapping
    public List<AfterSaleRequest> getByOrderId(@RequestParam Long orderId) {
        return afterSaleRepository.findByOrderId(orderId);
    }

    @GetMapping("/{id}")
    public AfterSaleRequest getById(@PathVariable Long id) {
        return afterSaleRepository.findById(id).orElse(null);
    }

    @PostMapping
    public AfterSaleRequest createAfterSaleRequest(@RequestBody AfterSaleRequest request) {
        return afterSaleRepository.save(request);
    }
}
